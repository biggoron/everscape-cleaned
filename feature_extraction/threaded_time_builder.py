import sqlite3 as lite
import time
import sys
import helpers as hp
from threaded_exclusive_zone import *
from multiprocessing import Process, Queue, Lock

# Defining the sessions to be analysed
global sessions
sessions = hp.sessions

# Cleans database and build a Time_choice table to store
# results
con = lite.connect('everscape.db')
with con :
    cur = con.cursor()
    try:
        cur.execute("\
            DROP TABLE Time_choice;\
        ")
        print("Database deleted")
    except:
        print("Still no Time_choice table to drop")

    cur.execute("\
        CREATE TABLE Time_choice (\
            session_id INTEGER,\
            avatar_no INTERGER,\
            mmss INTEGER,\
            choice INTEGER\
        );\
    ")

def get_time(session_index, avatar_index, avatar, tree, times):
# Gets the time of decision for avatar in session using the
# tree number tree. Stores it in times
    # Ask the finder to find the time with optimized
    # parameters
    returned_array = finder.time(\
        session_index, avatar_index, tree\
    )
    if len(returned_array) == 0:
    # if nothing found try "safe" mode.
        print("  retry %d, %d on %d" % \
            (session, avatar, tree))
        returned_array = finder.time(\
        session_index, avatar_index, tree, reduc_traj = 0\
        )
    if len(returned_array) == 0:
    # if still nothing found put alert
        print("  retried %d, %d on %d i n vain"%\
            (session_index, avatar_index, tree))
    token = 0
    for couple in returned_array:
    # stores result in shared memory
        token += 1
        decision = couple[1]
        time_decision = couple[0]
        times.put([\
            session_index, avatar, time_decision, decision])
    if token == 0:
        print("  alert session %d avatar %d"%(\
            session_index, avatar_index))

def finished(process):
# Helper to see if a process is finished. I put -1 if the
# process was not initiated
    if process == -1:
        return True
    if not process.is_alive():
        return True
    else:
        return False

choice_hashes = {}
con = lite.connect('everscape.db')
with con :
# Gets the choices of avatars
    cur =  con.cursor()
    cur.execute("\
        SELECT * FROM Path\
    ")
    rows = cur.fetchall()

# Tidy up the Choice data making a hash for each session
# containing as key the avatars, as value their choices
# These hashes are themselves stored in a hash.
for row in rows:
    try:
        choice_hashes[row[0]]
    except:
        choice_hashes[row[0]] = {}
    choice_hashes[row[0]][row [1]]=row[3]


# The computation is parallel. Each trajectory is analysed in
# a different subprocess. Each subprocess is given an argument
# with data to make computation on. Here are defined the
# arguments
arguments = []
for session in choice_hashes:
    session_index = sessions.index(session)
    avatars_choice = choice_hashes[session]
    avatar_array = hp.Avatar_of_session(session_index)
    for avatar in avatars_choice:
        if avatars_choice[avatar] == 0:
        # If an avatar didn't made a choice, there is no
        # decision time to compute.
            continue
        avatar_index = avatar_array.index(avatar)
        arguments.append([session_index, avatar_index, avatar])
# number of multiprocesses to use to make computation. 32 is
# rather good on my computer
nb = 32
# Builds the structure to make computation. comes from
# threaded_exclusive_zones.py
finder = TimeFinder(nb_trees = nb)
# memory shared among subprocesses
times = Queue()
# array referencing the subprocesses
p = []
for i in range(nb):
# initiating the array
    p.append(-1)
while not len(arguments) == 0:
# While their is still some computation to do ...
    cnt = 0
    for process in p:
    # look or an idle process ( or not initiated )
        if finished(process):
            if p[cnt] != -1:
            # finish an idle process properly
                p[cnt].join()
            if len(arguments) == 0:
            # if no more argument to compute go next
                continue
            # else take an argument and make a subprocess
            # compute the time of decision for it.
            argument = arguments.pop()
            argument.append(cnt)
            p[cnt] = Process(target=get_time,\
                args = (\
                    argument[0],\
                    argument[1],\
                    argument[2],\
                    argument[3],\
                    times))
            # run the subprocess
            p[cnt].start()
        cnt += 1

# Now all the arguments have been passed to a subprocess for
# computation. Lets wait for the subprocesses to finish
for process in p:
    if process != -1:
        process.join()

# Time to store the results
con = lite.connect('everscape.db')
with con :
    cur = con.cursor()
    while not times.empty():
    # Iterates over the results stored by the subprocesses
        line = times.get()
        # stores in database
        cur.execute("\
            INSERT INTO Time_Choice VALUES \
            (%d, %d, %d, %d);" % \
            (   sessions[line[0]],
                line[1],\
                line[2],\
                 line[3]\
             )\
         )

