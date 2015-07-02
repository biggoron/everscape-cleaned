#builds a KD tree with all the trajectory points, first choice
#A, then choice B. the indice of the limit between values
#belonging to A and belonging to B is recorded.
#builds a function to find the time at which a rtajectory
#enters a zone with a percentage of people from the same choice
#exceeding a threshold value. 
#Builds a helper function to compute the ratio at a given
#point.


import time
from operator import itemgetter
from multiprocessing import Process, Queue
import sys
import sqlite3 as lite
import dataset
from database_adapter import *
import matplotlib.pyplot as plt
from scipy import spatial as sp

class TimeFinder():

    def __init__(self, nb_trees = 4):
        #builds the KD-tree extracting people from choice
        #'train' on one hand, on choice 'car' (A or B) on the
        #other hand, concatening the points on each side, and
        #then concatening the two sides remembering the
        #junction indice.
        self.nb_trees = nb_trees

        car_array = []
        train_array = [] 
#        all_array = []

        choice_hashes = {}

        con = lite.connect('everscape.db')
        with con:
            cur = con.cursor()
            cur.execute("\
                SELECT * FROM Path\
            ")
            rows = cur.fetchall()

        for row in rows:
            try:
                choice_hashes[row[0]]
#                print("No session %d" % row[0])
            except:
                choice_hashes[row[0]] = {}
#                print("create session %d" % row[0])
            choice_hashes[row[0]][row[1]]=row[3]
#            print("put in session %d choice %d of avatar %d"%\
#                    (row[0], row[3], row[1]))
#            print("------------------------------")
#        print("++++++++++++++++++++++++++++++")

        for session in choice_hashes:
            if session == 14:
                continue
            session_id = dataset.a.index(session)
            logs = train_logs(session_id)
            avatars_choice = choice_hashes[session]
            for avatar in choice_hashes[session]:
                trajectory = Trajectory_points(session_id,\
                avatar)
                time_earthquake = earthquake_time(session_id)
#                print("Avatar %d of session %d made choice %d"%\
#                        (avatar, session, avatars_choice[avatar]))
                if (avatars_choice[avatar] == 1 or \
                    avatars_choice[avatar] == 2) and\
                    not requested_train(logs, avatar):
#                    print("classified car")
                    for point in trajectory:
                        if point[3] > time_earthquake:
                            car_array.append([point[0],\
                            point[1]])
#                            all_array.append([point[0],\
#                            point[1]])

                elif avatars_choice[avatar] == 3:
#                    print("classified train")
                    for point in trajectory:
                        if point[3] > time_earthquake:
                            train_array.append(\
                            [point[0], point[1]])
##                            all_array.append([point[0],\
#                            point[1]])
        
        self.limit = len(car_array)
        data = car_array
        for position in train_array:
            data.append(position)
        sys.setrecursionlimit(10000)
        self.trees = []
        for i in range(self.nb_trees):
            self.trees.append(-1)
        tree = sp.KDTree(data)
        for i in range(self.nb_trees):
            self.trees[i] = tree
        #multiple kdtrees should be used in multithreading,
        #it would else become the bottleneck as the time
        #factor in computation is due to kdtree lookups,
        #creating multiple KDtree is long and done before
        #any computation. Then we can multithread their
        #creation to gain some time.

    
    def car_ratio_calc(self, x, y, tree_nb):
        neighbours = self.trees[tree_nb].query_ball_point([x,y], 1)
        car_nb = 0
        train_nb = 0
        for neighbour in neighbours:
            if neighbour < self.limit:
                car_nb += 1
            else:
                train_nb += 1
        if car_nb + train_nb == 0:
            return -1
        else:
            car_ratio = float(car_nb) / float(car_nb + train_nb )
            return car_ratio

    def car_ratio_threaded(self, x, y, t, ratios, tree_nb):
        neighbours =\
        self.trees[tree_nb].query_ball_point([x,y], 0)
        car_nb = 0
        train_nb = 0
        for neighbour in neighbours:
            if neighbour < self.limit:
                car_nb += 1
            else:
                train_nb += 1
        if car_nb + train_nb == 0:
            return -1
        else:
            car_ratio = float(car_nb) / float(car_nb + train_nb )
            ratios.put([t, car_ratio])
            return car_ratio

    def car_ratios(self, trajectory, tree_nb):
        data = []
        for point in trajectory:
            data.append([point[0], point[1]])
        look_up = sp.KDTree(data)
        neighbours_list = look_up.query_ball_tree\
                            (self.trees[tree_nb], 1) 
#        print("computed neighbours list for %d" % len(data))
        ratios = []
        for neighbours in neighbours_list:
            car_nb = 0
            train_nb = 0
            for neighbour in neighbours:
                if neighbour < self.limit:
                    car_nb += 1
                else:
                    train_nb += 1
            if car_nb + train_nb == 0:
                ratios.append(-1)
            else:
                car_ratio = float(car_nb) /\
                float(car_nb + train_nb )
                ratios.append(car_ratio)
        return ratios
            

    def good_part(self, trajectory, tree_nb):
        low = 0
        high = len(trajectory)-1
        m = int((high-low)/2)
        while (high - low) > 40:
            span =trajectory[m-1 : m+3]
            pos1 = self.car_ratio_calc\
                (span[1][0],span[1][1], tree_nb)
            pos2 = self.car_ratio_calc\
                (span[0][0],span[0][1], tree_nb)
            pos3 = self.car_ratio_calc\
                (span[2][0],span[2][1], tree_nb)
            pos4 = self.car_ratio_calc\
                (span[3][0],span[3][1], tree_nb)
            cntA = 0
            cntB = 0
            if pos1 > 0.97:
                cntA += 1
            if pos2 > 0.97:
                cntA += 1
            if pos3 > 0.97:
                cntA += 1
            if pos4 > 0.97:
                cntA += 1
            if pos1 < 0.03:
                cntB += 1
            if pos2 < 0.03:
                cntB += 1
            if pos3 < 0.03:
                cntB += 1
            if pos4 < 0.03:
                cntB += 1

            if cntA > 2 or cntB > 2 and cntA != cntB:
                high = min(m + 2, high) 
                low = low
                m = int((high+low)/2)
            elif cntA == 0 and cntB == 0:
                high = high
                low = max(m - 2, low)
                m = int((high+low)/2)
            else :
                m = int((m+low)/2)
        return [low, high]
    
    def time(self, session_id, avatar_no,\
                tree_nb, reduc_traj = 1, threads = 1):
        print("in time function for avatar %d" % avatar_no)
        trajectory = Trajectory_points(session_id, avatar_no)
        trajectory_debug = Trajectory(session_id, avatar_no)
        print("trajectories loaded")
        time_earthquake = earthquake_time(session_id)
        time_token = 0
        for point in trajectory:
            if point[3] < time_earthquake:
                time_token += 1
            else:
                break
        trajectory = trajectory[time_token:]
        choices = []
        car_ratio_hist = [[],[]]
        decision_time_mem = []
        switch_token = 0
        i = 0
        if reduc_traj == 1:
            ind = self.good_part(trajectory, tree_nb)
            low = ind[0]
            high = ind[1]
            trajectory = trajectory[low : high]
#        else:
#            print("doing %d, %d on %d without reduc"%\
#                (session_id, avatar_no, tree_nb))

        car_ratio_mem1 = -1
        time_mem1 = -1
        car_ratio_mem2 = -1
        time_mem1 = -1
        car_ratio = -1
        time_mem = -1
        
        #find interesting subpart
        if threads != 1: 
            print("in threaded part")
            ratios = Queue()
            arguments = []
            for position in trajectory:
                arguments.append([position[0], position[1],\
                                position[3], ratios])
            print("arguments constructed")
            p = []
            time_token = 0
            for i in range(threads):
                p.append(-1)
            while not len(arguments) == 0:
                cnt = 0
                for process in p:
                    if process == -1 or not process.is_alive():
                        if p[cnt] != -1:
                            p[cnt].join()
                        if len(arguments) == 0:
                            continue
                        argument = arguments.pop()
                        argument.append(cnt)
                        print("doing time %d on thread %d"\
                            % (argument[2], argument[4]))
                        p[cnt] = Process(\
                            target=self.car_ratio_threaded,\
                            args = (argument[0],\
                                    argument[1],\
                                    argument[2],\
                                    argument[3],\
                                    argument[4]))
                        p[cnt].start()
                    cnt += 1
            time.sleep(10)
            infinite_loop = 1
            print("arguments exhausted")
            
            for process in p:
                process.join()

            while infinite_loop == 1:
            #    print("waiting for all processes to finish")
                token = 1
                counter = 0
                for process in p:
                    if process.is_alive():
                        print("process %d not finished" % counter)
                        token = 0
                    counter += 1
                if token == 1:
                    for process in p:
                        if process != -1:
                            process.join()
                    break
                else:
                    time.sleep(10)
            results = []
            while not ratios.empty():
                print("in_loop")
                results.append(ratios.get())
            results = sorted(results,key=itemgetter(0))
            print(results)
            car_ratios = []
            for result in results:
                car_ratios.append(result[1])
        else:
            car_ratios = self.car_ratios(trajectory, tree_nb)

        j = 0
        
        for position in trajectory:
#            if reduc_traj == 0:
#                print("doing %d of %d, %d on %d"%\
#                    (position[3], session_id, avatar_no, tree_nb))
            if position[3] < time_earthquake:
                continue
            if i == 0:
                i = 1
            
            car_ratio_mem2 = car_ratio_mem1
#            print("MEM2 TRACKING: %f" % car_ratio_mem2)
            time_mem2 = time_mem1
            car_ratio_mem1 = car_ratio
#            print("MEM1 TRACKING: %f" % car_ratio_mem1)
            time_mem1 = time_mem
            
            time_mem = position[3]
            car_ratio = car_ratios[j]
            if car_ratio == -1:
                continue
            
            
            if car_ratio_mem2 == -1:
                continue

            le = abs(car_ratio - car_ratio_mem2)
            li = min(abs(car_ratio - car_ratio_mem1), \
                    abs(car_ratio_mem1 - car_ratio_mem2))
#            print("%f || %f" % (le, li))
            if li > le:
#                print("change")
                car_ratio_mem1 = \
                (car_ratio_mem2 + car_ratio)/2.0
            car_ratio_hist[0].append(time_mem2)
            car_ratio_hist[1].append(car_ratio_mem2)
            if car_ratio_mem2 > 0.90 and switch_token != 1:
                choices.append([time_mem2, 1])
                switch_token = 1
                decision_time_mem.append(time_mem2)
            elif car_ratio_mem2 < 0.10 and switch_token != 2:
                choices.append([time_mem2, 2])
                switch_token = 2
                decision_time_mem.append(time_mem2)
            elif car_ratio_mem2 < 0.80 and car_ratio_mem2 >0.2:
                switch_token = 0
            #we are loosing the 2 last value of car_ratio,
            #never mind, a choice in the last two seconds is
            #not relevant
            j += 1
#        color_s = 0 
#        for i in range(len(car_ratio_hist[0])):
#            if car_ratio_hist[0][i] in decision_time_mem or \
#                color_s == 1:
#                plt.plot(car_ratio_hist[0][i],\
#                car_ratio_hist[1][i],\
#                'ro')
#                color_s = 1
#            else:
#                plt.plot(car_ratio_hist[0][i],\
#                car_ratio_hist[1][i],\
#                'bo')
#        plt.show()
#
#        color_s = 0 
#        for i in range(len(trajectory_debug[0])):
#            if trajectory_debug[3][i] in decision_time_mem\
#            or color_s == 1:
#                plt.plot(trajectory_debug[0][i],\
#                        trajectory_debug[1][i], 'ro')
#                color_s = 1
#            else:
#                plt.plot(trajectory_debug[0][i],\
#                trajectory_debug[1][i],\
#                'bo')
#        plt.show()
        return choices
