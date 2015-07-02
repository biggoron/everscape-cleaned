import matplotlib.pyplot as plt
import matplotlib.animation as animation
from database_adapter import *
import time
from helper import *

#define set of avatars in the same session
#get time of choice
#get trajectory
#define color for each avatar
#set loop executed once every 50ms
#in loop print a new point for each avatar
#in loop check if one of avatar is at turning point, if yes
#change color

def plot_choices(session_id):
    avatars = Avatar_of_session(session_id)
    trajectories = {}
    for avatar in avatars:
        trajectories[avatar] = Trajectory(session_id, avatar_no)


