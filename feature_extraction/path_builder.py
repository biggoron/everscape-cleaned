# This class classifies the roads taken by users.
# For the train it is obvious as we have some logs.
# For the path of those who have picked up a car, a KDtree is
# used. The procedure is supervised with some reference
# trajectory, but can be automatized with some more efforts.
# the references are 0,8 for road A
#                   0,6 for road B
# C is for train


import sqlite3 as lite
import matplotlib.pyplot as plt
from scipy import spatial as sp
import helpers as hp

class RoadClassifier:
    global sessions
    sessions = hp.sessions

    def __init__(self):
    # builds a KDTree filled with data extracted from avatar 8
    # in session 0.
    # the path A is the one taken by this avatar on the way on
    # ie : indices from 320 to 450 in the trajectory
    # the path B is the one taken by this avatar on the way back
    # ie : indices from 1200 to 1500 in the trajectory
        self.avatar_no = hp.Avatar_of_session(0)[8]
        self.data = hp.Trajectory_points(0, 8)
        # keeping for each point in trajectory only x and y
        self.data[:] = (elem[:2] for elem in self.data)

        self.minB = 1200
        self.maxB = 1500
        self.minA = 320
        self.maxA = 450
        self.tree = sp.KDTree(self.data)

    # The initialisation of path is the only non-automatic
    # part in the processing of data. Still it can be
    # automatized with a non-supervised algorithm by
    # playing with kdtree.
    # The principle would be to compare each new
    # trajectory to already existing trajectories for
    # close sub-segments of the trajectory. Close and long
    # enough sub-segments are on the same trajectory. To
    # find the span of the trajectory, one can make the
    # sub-segments grow until the growth makes the maximum
    # of the minimum distance between points too big.

    def classify(self, session_id, avatar_no, n_dist=30,\
    threshold=10):
    # Uses the KDTree to check neighbours at distance at max
    # n_dist of points in the trajectory of avatar_no in
    # session_id.
    # If a point has 100% of neighbours in A or in B, then
    # the path is A
    # ATTENTION PLEASE: do not use list of avatar, need to use
    # Avatar_of session
    # To classify one trajectory in A or B, the trajectory has
    # to offer more than [threshold] consecutive points
    # with only A or B neighbours in a radius n_dist 

        # taking the Trajectory points of this avatar
        traj = hp.Trajectory(session_id, avatar_no)
        # taking the time at which the avatar took the car on
        # the way on and on the way back
        before = hp.car_before(session_id, avatar_no)
        after = hp.car_after(session_id, avatar_no)

        # return a hash in the format:
        # {'before': 0/A/B, 'after':0/A/B}
        return_hash = {'before': 0, 'after':0}
        # store the time log of the the current position
        time = 0
        # stores the progress of the avatar (after/before
        # earthquake)
        state = 0
        # count the number of points verifying a 'in-path' criteria
        # in a row
        counter = 0
        # token assessing which path counter is referring to
        global_tokenA = True
        global_tokenB = True
        # number of consecutive point in a path to infer the
        # path
        avatar_list = hp.Avatar_of_session(session_id)
        print('session %d, avatar %d' % (\
                sessions[session_id], avatar_list[avatar_no]))
        print('before: %d' % before)
        print('after: %d' % after)
        print('max time: %d' % traj[3][-1])
        print(str(state))
        for i in range(len(traj[0])):
        # iterating over the position of the trajectory of the
        # avatar
            # timestamp of the current point in trajectory
            time = traj[3][i]
            # refresh state
            if before != -1 and state == 0 and time > before:
            #if after departing by car and still in state 0
            #(initial state) then change to 'way on' state
                state = 1
                print(str(state))
            if after != -1 and time > after and state != 2:
            # if after returning by car and not in state
            # 'returning' then change to 'way back' state
                state = 2
                print(str(state))

            if state == 1:
            # way on case
                tokenA = True
                tokenB = True
                # iterating over the neighbours of position
                # neighbours are referred to by their indices,
                # the range of acceptable indices for A and B
                # are known.
                for neighbours in \
                self.tree.query_ball_point(\
                [traj[0][i], traj[1][i]], n_dist):
                # examining the neighbours
                    if not neighbours or not\
                    (self.minA <= neighbours <= self.maxA):
                    # no neighbours or not all in A
                        tokenA = False
                    if not neighbours or not\
                    (self.minB <= neighbours <= self.maxB):
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
                if counter == threshold:
                # when a certain number of points in a row
                # are all in one path, then the path is
                # almost sure.
                # the finding is registered in the return_hash
                    if global_tokenA:
                        return_hash['before']='A'
                    if global_tokenB:
                        return_hash['before']='B'
                    counter = 0
                # state put on -1 to wait for the way back
                    state = -1
                    print(str(state))

            if state == 2:
            # the same for the return path,
                tokenA = True
                tokenB = True
                for neighbours in \
                self.tree.query_ball_point(\
                [traj[0][i], traj[1][i]], n_dist):
                    if not neighbours or not\
                    (self.minA <= neighbours <= self.maxA):
                        tokenA = False
                    if not neighbours or not\
                    (self.minB <= neighbours <= self.maxB):
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
                if counter == threshold:
                    if global_tokenA:
                        return_hash['after']='A'
                    if global_tokenB:
                        return_hash['after']='B'
                    counter = 0
                    # after deciding the returning way, return
                    # the return_hash result
                    print("time in 2 at end: %d" % time)
                    return return_hash
        print("time at end: %d" % time)
        return return_hash

    def store_in_table(self):
    # Compute and store in table Path the paths of all the
    # avatars of all the relevant sessions
        # cleaning and rebuilding the table
        con = lite.connect('everscape.db')
        with con:
            cur = con.cursor()
            try:
                cur.execute("\
                    DROP TABLE Path;\
                ")
            except:
                print('could not drop table Path')
            cur.execute("\
                CREATE TABLE Path(\
                    session_id INTEGER,\
                    avatar_no INTEGER,\
                    path_going INTEGER,\
                    path_returning INTEGER,\
                    PRIMARY KEY (session_id, avatar_no)\
                    );\
            ")
        global sessions
        print(sessions)
        avatar_llist = []
        path_hashes = []
        for session_index in range(len(sessions)):
        # iterating over the sessions
            avatar_llist.append(\
                hp.Avatar_of_session(session_index)\
            )
            path_hashes.append({})
            logs = hp.train_logs(session_index)
            # taking the index of the avatar
            avatar_index = 0
            for avatar in avatar_llist[-1]:
            #iterating over the avatars in one session
                # Find the way an avatar took on the way on
                # and the way back, if he took a car.
                print("")
                path = self.classify(session_index, avatar_index)
                print(path)
                if hp.granted_train(logs, avatar):
                # reads the train logs to check if the avatar
                # took the train on the way back
                    path['after']='C'
                # organizes all the info in a hash
                path_hashes[-1][avatar]=\
                            [path['before'], path['after']]
                # updating the index of the avatar
                avatar_index += 1

        con = lite.connect('everscape.db')
        with con:
        # Stores the hash containing all the info in the
        # database
            cur = con.cursor()
            for session_index in range(len(sessions)):
            # Iterating over sessions
                for avatar in avatar_llist[session_index]:
                # Iterating over the avatars in a session
                    before = path_hashes[session_index][avatar][0]
                    after = path_hashes[session_index][avatar][1]
                    if before == 'A':
                        before = 1
                    elif before == 'B':
                        before = 2
                    if after == 'A':
                        after = 1
                    elif after == 'B':
                        after = 2
                    elif after == 'C':
                        after = 3
                    cur.execute("\
                        INSERT INTO Path\
                        VALUES (%d, %d, %d, %d);"%(\
                            sessions[session_index],\
                            avatar,\
                            before,\
                            after\
                        )\
                    )

