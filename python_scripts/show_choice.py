from path_builder import *
import sqlite3 as lite
from database_adapter import *
from trajectory_plotting import *
import dataset

    
session_list = dataset.a
avatar_llist = []
path_hashes = []
classifier = RoadClassifier()
for session_id in range(len(session_list)): 
    avatar_llist.append(Avatar_of_session(session_id))
    path_hashes.append({})
    logs = train_logs(session_id)
    for avatar in Avatar_of_session(session_id):
        path = classifier.classify(session_id, avatar)
        if granted_train(logs, avatar):
            path['after']='C'
        path_hashes[-1][avatar]=[path['before'], path['after']]

con = lite.connect('everscape.db')
with con:
    cur = con.cursor()
    i = 0
    a=0
    for session_id in session_list: 
        print('!!! session ' + str(session_id) + ' !!!')
        a=0
        for avatar in avatar_llist[i]:
            before = path_hashes[i][avatar][0]
            after = path_hashes[i][avatar][1]
            print('avatar ' + str(avatar) + ': ' +\
                str(before) + ', ' + str(after))
            input('')
            Trajectory2D_plot(i, a)
            a = a+1
        i = i + 1

