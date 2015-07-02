import sqlite3 as lite
import time
import sys
from dataset import *
from database_adapter import *
from threaded_exclusive_zone import *
from trajectory_plotting import *
from multiprocessing import Process, Queue, Lock

con = lite.connect('everscape.db')
with con :
    cur = con.cursor()
    try:
        cur.execute("\
            DROP TABLE Time_choice3;\
        ")
        print("Database deleted")
    except:
        print("Still no Time_choice table to drop")

    cur.execute("\
        CREATE TABLE Time_choice3 (\
            session_id INTEGER,\
            avatar_no INTERGER,\
            mmss INTEGER,\
            choice INTEGER\
        );\
    ")

def get_time(session, avatar, tree, times):
    returned_array = finder.time(session, avatar, tree)
    if len(returned_array) == 0:
        print("  retry %d, %d on %d" %\
            (session, avatar, tree))
        returned_array = finder.time(session, avatar, tree, reduc_traj = 0)
    if len(returned_array) == 0:
        print("  retried %d, %d on %d in vain"%\
            (session, avatar, tree))
    token = 0
    for couple in returned_array:
        token += 1
        decision = couple[1]
        time_decision = couple[0]
        times.put([session, avatar, time_decision, decision])
    if token == 0:
        print("  alert session %d avatar %d"%(session, avatar))

def finished(process):
    if process == -1:
        return True
    if not process.is_alive():
        return True
    else:
        return False

choice_hashes = {}
con = lite.connect('everscape.db')
with con :
    cur = con.cursor()
    cur.execute("\
        SELECT * FROM Path\
    ")
    rows = cur.fetchall()

#print("choices imported")

for row in rows:
    try:
        choice_hashes[row[0]]
    except:
        choice_hashes[row[0]] = {}
    choice_hashes[row[0]][row[1]]=row[3]

#print("choices hash constructed")

arguments = []
for session in choice_hashes:
    if session == 14:
        continue
    session_id = dataset.a.index(session)
    avatars_choice = choice_hashes[session]
    for avatar in avatars_choice:
#        print("Doing avatar %d" % avatar)
        if avatars_choice[avatar] == 0:
            continue
        arguments.append([session_id, avatar])
#print("Arguments initialized")

nb = 32
finder = TimeFinder( nb_trees = nb)
#print("Tree initialized")
times = Queue()
p = []
for i in range(nb):
    p.append(-1)
while not len(arguments) == 0:
    cnt = 0
    for process in p:
        if finished(process):
            if p[cnt] != -1:
                p[cnt].join()
            if len(arguments) == 0:
                continue
            argument = arguments.pop()
            argument.append(cnt)
#            print("affecting process %d, %d to %d" % \
#                (argument[0], argument[1], cnt))
            p[cnt] = Process(target=get_time,\
                args = (argument[0], argument[1], argument[2], times))
            p[cnt].start()
        cnt += 1

infinite_loop = 1
while infinite_loop == 1:
#    print("waiting for all processes to finish")
    token = 1
    counter = 0
    for process in p:
        if not finished(process):
            print("process %d not finished" % counter)
            token = 0
        counter += 1
    if token == 1:
        for process in p:
            if process != -1:
                process.join()
        break
    else:
        time.sleep(100)

print("store in database")
con = lite.connect('everscape.db')
with con :
    cur = con.cursor()
    while not times.empty():
        line = times.get()
        cur.execute("\
            INSERT INTO Time_Choice3 VALUES \
            (%d, %d, %d, %d);" % \
            (   line[0],
                line[1],\
                line[2],\
                line[3]\
            )\
        )

