# The goal is to find when people make the first choice
# between train and car. the same method can be applied to the
# choice between the 2 possible roads by car.
# Builds a pool of KD trees with all the trajectory points,
# first corresponding to choice A, then choice B. the indice
# of the limit between values Belonging to A and belonging to B
# is recorded.
# Builds a function to find the time at which a trajectory
# enters a zone with a percentage of people from the same choice
# exceeding a threshold value. 
# Builds a helper function to compute the ratio at a given
# point.


import time
from operator import itemgetter
from multiprocessing import Process, Queue
import sys
import sqlite3 as lite
import helpers as hp
from scipy import spatial as sp

class TimeFinder():

    # Contains the session numbers that are valid for analysis
    global sessions
    sessions = hp.sessions

    def __init__(self, nb_trees = 4):
        #builds the KD-tree extracting people from choice
        #'train' on one hand, on choice 'car' (A or B) on the
        #other hand, concatening the points on each side, and
        #then concatening the two sides remembering the
        #junction indice.
        self.nb_trees = nb_trees

        car_array = []
        train_array = []

        choice_hashes = {}

        con = lite.connect('everscape.db')
        with con:
        # Loading the choices of avatars
            cur = con.cursor()
            cur.execute("\
                SELECT * FROM Path\
            ")
            rows = cur.fetchall()

        for row in rows:
        # Stores and sorts those choices in hashes
            try:
            # Ensures the hash corresponding to the sessions
            # is created, else creates it.
                choice_hashes[row[0]]
            except:
                choice_hashes[row[0]] = {}
            # For each session hash, the key is the avatar,
            # the value is its choice.
            # Here all the sessions and avatar numbers are
            # real numbers, not the indices
            choice_hashes[row[0]][row[1]]=row[3]

        for session in choice_hashes:
        # Iterating over the sessions, here the session
        # variable is a hash (iterating over an array of
        # hashes
            # Getting the index of the session in order to be
            # able to get the hash containing the choices made
            # by the avatars during the session
            session_index = sessions.index(session)
            # Train logs. Not only people who choose train
            # went to the train station. Some other people
            # choose to go to the station but were not granted
            # a seat. In the scope of this analysis we
            # consider they made the choice to go to the
            # station.
            logs = hp.train_logs(session_id)
            # Getting the hash containing the choices of the
            # avatars in the session.
            avatars_choice = choice_hashes[session]
            # Usefull to retrieve the index of the avatars
            avatar_array = Avatar_of_session(session_index)
            for avatar in avatars_choice:
            # Iterating in this hash
                # Usefull to call the method from helpers file
                avatar_index = avatar_array.index(avatar)
                # Getting the trajectory of the considered
                # avatar.
                trajectory = hp.Trajectory_points(session_index,\
                avatar_index)
                # We only take the part of the trajectory
                # after the earthquake. If the avatar went by
                # car and returned by train, mingling the two
                # parts of the trajectory is problematic.
                time_earthquake =\
                    hp.earthquake_time(session_index)
                if (avatars_choice[avatar] == 1 or \
                    avatars_choice[avatar] == 2) and\
                    # Carefull, some people who took a car
                    # went first to the train station. We
                    # don't want to take those people into
                    # account to build a tree against which we
                    # will look up trajectories.
                    not hp.requested_train(logs, avatar):
                    for point in trajectory:
                        if point[3] > time_earthquake:
                        # Only the part of trajectory after
                        # earthquake is usefull.
                            car_array.append([point[0],\
                            point[1]])
#                            all_array.append([point[0],\
#                            point[1]])

                elif avatars_choice[avatar] == 3:
#                    print("classified train")
                    for point in trajectory: 
                        if point[3] > time_earthquake:
                        # Only the part of trajectory after
                        # earthquake is usefull.
                            train_array.append (\
                            [point[0], point[1]])
        # When I will ask the tree for neighbours, the tree
        # will give back indices of the data points
        # corresponding to neighbours. As I will concatene
        # the data points from car user with data points from
        # train users, I have to keep track of the limit
        # indice between both dataset in order to trace which
        # indices correspond to which dataset
        self.limit = len(car_array)
        # Here we concatene the to datasets
        data = car_array
        for position in train_array:
            data.append(position)
        # Building a KDTree is recursive and here we have some
        # volume
        sys.setrecursionlimit(10000)
        # Building many times the same tree (it is fast) so
        # that later, for slow parts of the program we can
        # make parallel computing (to compute the time of
        # decision).
        self.trees = []
        for i in range(self.nb_trees):
            self.trees.append(-1)
        tree = sp.KDTree(data)
        for i in range(self.nb_trees):
            self.trees[i] = tree
        # Multiple kdtrees should be used in multithreading,
        # it would else become the bottleneck as the time
        # factor in computation is due to kdtree lookups,
        # creating multiple KDtree is not so long and done before
        # any computation. 

    def car_ratio_calc(self, x, y, tree_nb):
    # Make some lookups on the tree number tree_nb to compute
    # the ratio of people taking car on people taking train
    # within the neighbours of point (x, y)
        neighbours = self.trees[tree_nb].query_ball_point([x,y], 1)
        car_nb = 0
        train_nb = 0
        for neighbour in neighbours:
            if neighbour < self.limit:
            # Car user
                car_nb += 1
            else:
            # Train user
                train_nb += 1
        if car_nb + train_nb == 0:
        # no neighbours
            return -1
        else:
        # compute ratio
            car_ratio = float(car_nb) / float(car_nb + train_nb )
            return car_ratio

    def car_ratio_threaded(self, x, y, t, ratios, tree_nb):
    # Computes the ratio of nieghbours choosing car one point
    # at a time but in parallel. Queryin neighbours against
    # tree number tree_nb. Do not use if the procedure is
    # already parallelized accross trajectories.
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
    # Compute the ratio of neighbours choosing car for all
    # points in a trajectory
        # organise trajectory points in a tree shape
        data = []
        for point in trajectory:
            data.append([point[0], point[1]])
        look_up = sp.KDTree(data)
        # Query tree against tree for neighbours (faster than
        # point by point)
        neighbours_list = look_up.query_ball_tree\
                            (self.trees[tree_nb], 1) 
        ratios = []
        for neighbours in neighbours_list:
        # now that i have the neighbours, i compute the ratios
        # one neighbour at a time.
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
    # reduces the span over which I scan the trajectory to
    # find the time of choice by dichotomic search. As a probe
    # to check if the transition already past or yet to come i
    # use a 4 timestamps wide check, in order to be more
    # robust.
        # initial low indice of the reduced range
        low = 0
        # initial high indice of the reduced range
        high = len(trajectory)-1
        # middle of the actual range, the place to check in
        # order to reduce the range in a dichotomic search
        m = int((high-low)/2)
        while (high - low) > 40:
        # I want to obtain at the end a reduced range roughly
        # around 40 timestamps long.
            # Building a checking span around the m position
            span =trajectory[m-1 : m+3]
            # computing the ratios in the span area
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
            # counting the number of "extreme" points, to see
            # if the choice is already done or yet to come.
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
            # the choice has already been done: so lets reduce
            # the span to low -> m
                high = min(m + 2, high)
                low = low
                m = int((high+low)/2)
            elif cntA == 0 and cntB == 0:
            # the choice has not yet been done: so lets reduce
            # the span to m -> high
                high = high
                low = max(m - 2, low)
                m = int((high+low)/2)
            else :
            # The situation is unclear, maybe some noise or
            # strange situation. Lets move m within the range
            # low -> high to see if it gets clearer.
                 m = int((m+low)/2)
        return [low, high]

    def time(self, session_index, avatar_index,\
                tree_nb, reduc_traj = 1, threads = 1 ):
    # Method called many times in parallel to compute the time
    # at which avatar made decision. reduc_traj is a boolean
    # to decide if we introduce some dichotomic search to find
    # the time of choice. Threads is the number of threads
    # used.
    # tree_nb is the number of the look up tree allocated to
    # the current subprocess.
        trajectory = hp.Trajectory_points(\
            session_index,\
            avatar_index)
        # I am only interested in the trajectory after
        # earthquake
        time_earthquake = hp.earthquake_time(session_index)
        time_token = 0
        for point in trajectory:
            if point[3] < time_earthquake:
                time_token += 1
            else:
                break
        trajectory = trajectory[time_token:]
        # An avatar can make more than one choice. Going for
        # the train, being refused a seat, going then to a
        # car.
        choices = []
        # Memory to store the decision_times corresponding to
        # the choices
        decision_time_mem = []
        i = 0
        if reduc_traj == 1:
        # Reduces greatly the span in which to search for the
        # time of decision. Makes the search much faster.
            ind = self.good_part(trajectory, tree_nb)
            low = ind[0]
            high = ind[1]
            trajectory = trajectory[low : high]
        # memories used to apply a filter on the series of
        # ratios within the neighbours. removing noise without
        # smoothing the transition corresponding to the
        # decision time.
        car_ratio_mem1 = -1
        time_mem1 = -1
        car_ratio_mem2 = -1
        time_mem1 = -1
        car_ratio = -1
        time_mem = -1
        #find interesting subpart
        if threads != 1:
        # I use the word thread because it is short but the
        # correct term is subprocess. multi-threading in
        # python still uses only one interpreter which is
        # limited to one process on the computer and doesn't
        # much improvement on computation time.
        # multi-processing is much more powerfull as it
        # duplicates the python interpreter itselfs into many
        # processes.
            # Shared memory across processes.
            ratios = Queue()
            arguments = []
            for position in trajectory:
            # prepares the arguments to pass to subprocesses
            # for computation
                arguments.append([position[0] , position[1],\
                                position[3], ratios])
            # array used as memory to store subprocesses
            p = []
            for i in range(threads):
            # Giving the good length to the array
                p.append(-1)
            while not len(arguments) == 0:
            # While there is some arguments to be passed for
            # computation...
                cnt = 0
                for process in p:
                # iterate over the processes
                    if process == -1 or not process.is_alive():
                    # If one is idled or not yet instantiated
                        if p[cnt] != -1:
                        # finish it properly if idled
                            p[cnt].join()
                        if len(arguments) == 0:
                        # if no more arguments to pass, then
                        # go next
                            continue
                        # else pass one argument to the
                        # subprocess for computation
                        argument = arguments.pop()
                        argument.append(cnt)
                        p[cnt] = Process(\
                            target=self.car_ratio_threaded,\
                            args = (argument[0],\
                                    argument[1],\
                                    argument[2],\
                                    argument[3],\
                                    argument[4]))
                        p[cnt].start()
                    cnt += 1
            # When no more arguments, it can take a while to
            # wait for all the currently running subprocesses
            # to finish, let's wait a little
            for process in p:
                process.join()

            results = []
            while not ratios.empty():
            # The computed ratios where stored in shared
            # memory, lets unpack this memory
                results.append(ratios.get())
            # The computing being done in parallel, the ratios
            # are not in the good order, lets order it.
            results = sorted(results,key=itemgetter(0))
            car_ratios = []
            for result in results:
                car_ratios.append(result[1])
        else:
        # if the procedure is not done in parallel, it is much
        # simpler ...
            car_ratios = self.car_ratios(trajectory, tree_nb)
        # index of position in trajectory during the loop
        j = 0
        # used for applying a filter
        switch_token = 0
        for position in trajectory:
            # Applying filter to smooth noise without
            # smoothing the transition corresponding to the
            # choice
            if position[3] < time_earthquake:
                continue
            if i == 0:
                i = 1
            car_ratio_mem2 = car_ratio_mem1
            time_mem2 = time_mem1
            car_ratio_mem1 = car_ratio
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
            if li > le:
                car_ratio_mem1 = \
                (car_ratio_mem2 + car_ratio)/2.0
            car_ratio_hist[0].append(time_mem2)
            car_ratio_hist[1].append(car_ratio_mem2)
            if car_ratio_mem2 > 0.90 and switch_token != 1:
            # seems to have choosen car
                choices.append([time_mem2, 1])
                switch_token = 1
                decision_time_mem.append(time_mem2)
            elif car_ratio_mem2 < 0.10 and switch_token != 2:
            # seems to have choosen train
                choices.append([time_mem2, 2])
                switch_token = 2
                decision_time_mem.append(time_mem2)
            elif car_ratio_mem2 < 0.80 and car_ratio_mem2 >0.2:
            # no obvious choice
                switch_token = 0
            #we are loosing the 2 last value of car_ratio,
            #never mind, a choice in the last two seconds is
            #not relevant
            j += 1
        return choices
