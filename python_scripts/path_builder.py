# stores reference paths in a special table:
# uses this table to build another table containing
# the car path taken by users who took car, after and before
# earthquake
# the references are 0,8 for road A
#                   0,6 for road B

# C is for train


import sqlite3 as lite
import dataset
from database_adapter import *
import matplotlib.pyplot as plt
from scipy import spatial as sp

class RoadClassifier:

    def __init__(self):
        # builds a KDTree filled with data extracted from avatar 8
        # in session 0.
        # the path A is the one taken by this avatar on the way on
        # ie : indices from 320 to 450 in the trajectory
        # the path B is the one taken by this avatar on the way back
        # ie : indices from 1200 to 1500 in the trajectory
        self.avatar_no = Avatar_of_session(0)[8]
        self.data = Trajectory(0, self.avatar_no)
        self.X = self.data[0]
        self.Y = self.data[1]

        self.minB = 1200
        self.maxB = 1500
        self.minA = 320
        self.maxA = 450
        self.min_set = 0
        self.max_set = len(self.X)

        #plt.plot(X[min:max], Y[min:max], 'go')
        #plt.plot(X[min1:max1], Y[min1:max1], 'bo')
        #plt.plot(X[min2:max2], Y[min2:max2], 'ro')
        #plt.show()#
        points = []
        for i in range(len(self.X)):
            points.append([self.X[i], self.Y[i]])
        self.tree = sp.KDTree(points)

    # Uses the KDTree to check neighbours at distance at max n_dist of points
    # in the trajectory of avatar_no in session_id.
    # If a point has 100% of neighbours in A or in B, then the path including
    # including the trajectory is A or B.
    # ATTENTION PLEASE: do not use list of avatar, need to use Avatar_
    # oof_session extrenall # ATTENTION PLEASE: do not use list of avatar, need to use Avatar_
    # oof_session externally
    def classify(self, session_id, avatar_no, n_dist=30):

        # taking the Trajectory points of this avatar
        traj = Trajectory(session_id, avatar_no)
        # taking the time at which the avatar took the car on the way on and
        # on the way back
        before = car_before(session_id, avatar_no) 
        after = car_after(session_id, avatar_no) 

        # return a hash in the format:
        # {'before': 0/A/B, 'after':0/A/B}
        return_hash = {'before': 0, 'after':0}
        
        # store the time log of the the current position
        time = 0
        # stores the progress of the avatar (after/before earthquake)
        state = 0
        # count the number of points verifying a 'in-path' criteria
        # in a row
        counter = 0
        # token assessing which path counter is referring to
        global_tokenA = True
        global_tokenB = True
        
        # number of consecutive point in a path to infer the
        # path
        criteria = 10 
        for i in range(len(traj[0])):
            # timestamp of the current point in trajectory
            time = traj[3][i] 
            # refresh state
            if before != -1 and state == 0 and time > before:
                #if after departing by car and still in state 0
                #(initial state) then change to 'way on' state
                state = 1
            if after != -1 and time > after and state != 2:
                # if after returning by car and not in state 'returning'
                # then change to 'way back' state
                state = 2
            
            if state == 1:
                # way on case
                tokenA = True
                tokenB = True
                # iterating over the neighbours of position
                # neighbours are referred to by their indices,
                # the range of acceptable indices for A and B are known.
                for neighbours in \
                self.tree.query_ball_point(\
                [traj[0][i], traj[1][i]], n_dist):
                    if not neighbours or not (self.minA <= neighbours <= self.maxA):
                        # no neighbours or not all in A
                        tokenA = False
                    if not neighbours or not (self.minB <= neighbours <= self.maxB):
                        # no neighbours or not all in B
                        tokenB = False
                if tokenA and global_tokenA :
                    # One more point in a series of A point
                    counter += 1
                    global_tokenB = False
                elif tokenB and global_tokenB :
                    # One more point in a series of B point
                    counter += 1
                    global_tokenA = False
                elif tokenA:
                    # first point in a A series
                    global_tokenB = False
                    global_tokenA = True
                    counter = 0
                elif tokenB:
                    # first point in a A series
                    global_tokenA = False
                    global_tokenB = True
                    counter = 0
                else:
                    # point that is neither in A nor in B
                    global_tokenA = False
                    global_tokenB = False
                    counter = 0
                if counter == criteria:
                    # when 10 points in a row are all in one path,
                    # then then path is almost sure.
                    # the finding is registered in the return_hash
                    if global_tokenA:
                        return_hash['before']='A'
                    if global_tokenB:
                        return_hash['before']='B'
                    counter = 0
                    state = -1

            if state == 2:
                # the same for the return path,
                # should be simplified with an external private function
                # accessed with two arguments: After/before.
                # TODO
                tokenA = True
                tokenB = True
                for neighbours in \
                self.tree.query_ball_point(\
                [traj[0][i], traj[1][i]], n_dist):
                    if not neighbours or not (self.minA <= neighbours <= self.maxA):
                        tokenA = False
                    if not neighbours or not (self.minB <= neighbours <= self.maxB):
                        tokenB = False
                if tokenA and global_tokenA :
                    counter += 1
                    global_tokenB = False
                elif tokenB and global_tokenB :
                    counter += 1
                    global_tokenA = False
                elif tokenA:
                    global_tokenB = False
                    global_tokenA = True
                    counter = 0
                elif tokenB:
                    global_tokenA = False
                    global_tokenB = True
                    counter = 0
                else:
                    global_tokenA = False
                    global_tokenB = False
                    counter = 0
                if counter == criteria:
                    if global_tokenA:
                        return_hash['after']='A'
                    if global_tokenB:
                        return_hash['after']='B'
                    counter = 0
                    #after deciding the returning way, return
                    #the return_hash result
                    return return_hash
        return return_hash

