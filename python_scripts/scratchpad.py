import matplotlib.pyplot as plt
import database_adapter
from trajectory_plotting import *
from database_adapter import *
from path_builder import *
from threaded_exclusive_zone import *
import time
from multiprocessing import Process, Queue
import os

Trajectory2DTimeAll_plot(0)

#
#finder = TimeFinder(32)
#print("finder built")
#choice_hashes = {}
#con = lite.connect('everscape.db')
#with con :
#    cur = con.cursor()
#    cur.execute("\
#        SELECT avatar_no FROM Path where\
#        session_id = 12 and path_returning != 0\
#    ")
#    rows = cur.fetchall()
#avatars = []
#for avatar in rows:
#    avatars.append(avatar[0])
#time_decision =\
#    finder.time(0, avatars[2], 0, reduc_traj = 1, threads =32) 
#    
#
#print(str(finder.time(5,7)))
#Trajectory2D_plot(5,7)
#Print_axis_all(2, axis='z')
#print(info_session(5))
#print(train_logs(0)) 
