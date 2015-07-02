#builds a KD tree with all the trajectory points, first choice
#A, then choice B. the indice of the limit between values
#belonging to A and belonging to B is recorded.
#builds a function to find the time at which a rtajectory
#enters a zone with a percentage of people from the same choice
#exceeding a threshold value. 
#Builds a helper function to compute the ratio at a given
#point.


import sys
import sqlite3 as lite
import dataset
from database_adapter import *
import matplotlib.pyplot as plt
from scipy import spatial as sp

class TimeFinder:
    class TreeBuilderThread (threading.Thread):
        def __init__(self, finder, id):
            threading.Thread.__init__(self)
            self.threadID = id
        def run(self, data):
            print("beginning to build tree %d" % self.threadID)
            print(len(data))
            #TODO make calculus

    def __init__(self):
        #builds the KD-tree extracting people from choice
        #'train' on one hand, on choice 'car' (A or B) on the
        #other hand, concatening the points on each side, and
        #then concatening the two sides remembering the
        #junction indice.

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
        self.tree = sp.KDTree(data)
#        self.look_up = sp.KDTree(all_array)
    
        #multiple kdtrees should be used in multithreading,
        #it would else become the bottleneck as the time
        #factor in computation is due to kdtree lookups,
        #creating multiple KDtree is long and done before
        #any computation. Then we can multithread their
        #creation to gain some time.

    
    def car_ratio_calc(self, x, y):
        neighbours = self.tree.query_ball_point([x,y], 1)
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

    def car_ratios(self, trajectory):
        data = []
        for point in trajectory:
            data.append([point[0], point[1]])
        look_up = sp.KDTree(data)
        neighbours_list = look_up.query_ball_tree(self.tree, 1) 
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
            

    def good_part(self, trajectory):
        low = 0
        high = len(trajectory)-1
        m = int((high-low)/2)
        while (high - low) > 40:
            span =trajectory[m-1 : m+3]
            pos1 = self.car_ratio_calc(span[1][0],span[1][1])
            pos2 = self.car_ratio_calc(span[0][0],span[0][1])
            pos3 = self.car_ratio_calc(span[2][0],span[2][1])
            pos4 = self.car_ratio_calc(span[3][0],span[3][1])
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

    def time(self, session_id, avatar_no):
        trajectory = Trajectory_points(session_id, avatar_no)
        time_earthquake = earthquake_time(session_id)
        choices = []
        car_ratio_hist = [[],[]]
        switch_token = 0
        i = 0
        ind = self.good_part(trajectory)
        low = ind[0]
        high = ind[1]
        trajectory = trajectory[low : high]

        car_ratio_mem1 = -1
        time_mem1 = -1
        car_ratio_mem2 = -1
        time_mem1 = -1
        car_ratio = -1
        time_mem = -1
        
        #find interesting subpart
        
        car_ratios = self.car_ratios(trajectory)

        j = 0
        
        for position in trajectory:
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
#            car_ratio = self.car_ratio_calc(position[0],\
#                                            position[1])
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
            elif car_ratio_mem2 < 0.10 and switch_token != 2:
                choices.append([time_mem2, 2])
                switch_token = 2
            elif car_ratio_mem2 < 0.80 and car_ratio_mem2 >0.2:
                switch_token = 0
            #we are loosing the 2 last value of car_ratio,
            #never mind, a choice in the last two seconds is
            #not relevant
            j += 1
#        plt.plot(car_ratio_hist[0], car_ratio_hist[1],\
#        marker='o')
#        plt.show()
        return choices
