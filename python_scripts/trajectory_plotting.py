import math
from mpl_toolkits.mplot3d import Axes3D
import dataset
from database_adapter import *
import matplotlib.pyplot as plt
import numpy as np
import helpers
#Mining of evescape.db

#Plot Trajectory from player i:
def Trajectory_plot(session_id, avatar_no):
    avatar_no = Avatar_of_session(session_id)[avatar_no]
    data = Trajectory(session_id, avatar_no)
    X = data[0]
    Y = data[1] 
    Z = data[2]
    C = [] 
    norm = len(X)
    print(str(norm))
    #color cycle params
    freq = 2.0*math.pi/float(norm)

    for i in range(norm):
        color = Color_cycle(i,freq)
        C.append(color)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(len(X)):
        ax.scatter(X[i], Y[i], Z[i], c=C[i], marker='o')

    plt.show()

def Trajectory2D_plot(session_id, avatar_no):
    avatar_no = Avatar_of_session(session_id)[avatar_no]
    data = Trajectory(session_id, avatar_no)
    X = data[0]
    Y = data[1] 
    C = [] 
    norm = len(X)
    #color cycle params
    freq = 2.0*math.pi/float(norm)

    for i in range(norm):
        color = Color_cycle(i,freq)
        C.append(color)
    plt.plot(X, Y, marker='o')

    plt.show()

def Trajectory2DTime_plot(session_id, avatar_no):
    avatar_no = Avatar_of_session(session_id)[avatar_no]
    avatars, mmss, choices = TimeChoice(session_id)
    print (avatars)
    if not (avatar_no in avatars):
        choice_time = -1
        print("Avatar didn't made a choice")
    else:
        choice_time = mmss[avatars.index(avatar_no)]
        print("Choice %d made at time %d" % \
                (choices[avatars.index(avatar_no)], choice_time))
    data = Trajectory(session_id, avatar_no)
    X = data[0]
    Y = data[1] 
    T = data[3]
    C = [] 
    norm = len(X)
    #color cycle params

    state = 0
    for i in range(norm):
        if T[i] == choice_time:
            print("ca colle")
            state = 1
        if state == 0:
            plt.plot(X[i], Y[i], 'bs')
        else:
            plt.plot(X[i], Y[i], 'rs')
    plt.show()

def Trajectory2DTimeAll_plot(session_id):
    avatars, mmss, choices = TimeChoice(session_id)
    print (avatars)
    for avatar in avatars:
        choice_time = mmss[avatars.index(avatar)]
        data = Trajectory(session_id, avatar)
        X = data[0]
        Y = data[1] 
        T = data[3]
        C = [] 
        norm = len(X)
        #color cycle params

        state = 0
        for i in range(norm):
            if T[i] >= choice_time:
                plt.plot(X[i], Y[i], 'bs')
    plt.show()

def Trajectory2DOnlyTime_plot(session_id):
    list_avatars = Avatar_of_session(session_id)
    avatars, mmss, choices = TimeChoice(session_id)
    print (avatars)
    for avatar in avatars:
        choice_time = mmss[avatars.index(avatar)]
        data = Trajectory(session_id, avatar)
        X = data[0]
        Y = data[1] 
        T = data[3]
        C = [] 
        norm = len(X)
        #color cycle params

        state = 0
        for i in range(norm):
            if T[i] == choice_time:
                plt.plot(X[i], Y[i], 'b.')
    plt.show()

#print all trajectories
def Trajectories_plot(session_id, liminf=0, limsup='none'):
    fig = plt.figure()
    avatar_array = Avatar_of_session(session_id)

    if type(limsup) is int and limsup <= len(avatar_array) and limsup >= liminf:
        avatar_array = avatar_array[liminf:limsup]

    C = [] 
    
    #color cycle params
    freq = 2.0*math.pi/float(len(avatar_array))
    
    for j in range(len(avatar_array)):
        color = Color_cycle(j,freq)
        C.append(color)
    ax = fig.add_subplot(111, projection='3d')

    j=0
    for avatar_no in avatar_array:
        data = Trajectory(session_id, avatar_no)
        X = data[0]
        Y = data[1]
        Z = data[2]
        
        for i in range(len(X)):
            ax.scatter(X[i], Y[i], Z[i], c=C[j], marker='o')
        j=j+1
    
    plt.show()

#print x series for an avatar
def Print_axis(session_id, avatar_no, axis='x'):
    avatar_array = Avatar_of_session(session_id)
    avatar_no = avatar_array[avatar_no]
    if axis == 'x':
        data = x_series(session_id, avatar_no)
    elif axis == 'y':
        data = y_series(session_id, avatar_no)
    elif axis == 'z':
        data = z_series(session_id, avatar_no)
    else:
        print('axis can be x, y or z only')
        return

    plt.plot(data[0], data[1], linestyle="-")
    plt.show()

    
def Print_axis_all(session_id, axis='x', liminf=0, limsup='none'):
    avatar_array = Avatar_of_session(session_id)
    C = []
    if type(limsup) is int and limsup <= len(avatar_array) and limsup >= liminf:
        avatar_array = avatar_array[liminf:limsup]
        
    #color cycle param
    freq = 2.0*math.pi/float(len(avatar_array))

    for i in range(len(avatar_array)):
        color = Color_cycle(i, freq)
        C.append(color)
    
    for i in range(len(avatar_array)):
        if axis == 'x':
            data = x_series(session_id, avatar_array[i])
        elif axis == 'y':
            data = y_series(session_id, avatar_array[i])
        elif axis == 'z':
            data = z_series(session_id, avatar_array[i])
        else:
            print('axis can be x, y or z only')
            return
        plt.plot(data[0], data[1], c=C[i], linestyle="-")
    
    plt.show()

    
