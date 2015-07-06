# This file contains all the helpers used to make other files
# clearer and less repetitive.

import math
import binascii
import matplotlib.pyplot as plt
import sqlite3 as lite
from mpl_toolkits.mplot3d import Axes3D

# All sessions were not actual experiments. Some were done to
# test or show the simulation software. Then I want to
# discard the sessions in which there is no "behaviour" to
# analyse. I threw out sessions with too few avatars, not
# lasting long enough or with no earthquake. This results in
# the following array of session ids which lists the relevant
# sessions.
# Also, thanks to this array, I will be able to reffer to the
# first relevant session by hp.sessions[1] where hp stands for
# helpers (include helpers as hp)
# From 26 sessions, we go down to 11 sessions with at least 10
# minutes of experiments, 20 users, and an earthquake
# happening after everyone has been forced to assist the
# concert event.
global sessions
sessions = [12, 13, 18, 19, 20, 21, 22, 23, 24, 25, 26]

# Helper to pick color automatically or plots
# Cycling throught color cycle
# returns a #RRGGBB string in hexadecimal notation
# blue -> green -> red
def Color_cycle(i, freq):
    p = math.pi*2.0/3.0
    red = math.sin(freq*i) * 127 + 128
    green = math.sin(freq*i + p) * 127 + 128
    blue = math.sin(freq*i + 2.0 * p) * 127 + 128
    red_str = hex(int(red))[2:]
    if len(red_str)  == 1:
        red_str = '0'+red_str
    green_str = hex(int(green))[2:]
    if len(green_str)  == 1:
        green_str = '0'+green_str
    blue_str = hex(int(blue))[2:]
    if len(blue_str)  == 1:
        blue_str = '0'+blue_str
    return '#' + red_str + green_str + blue_str

# Helpers to compute distances
def Distance3D(X1, Y1, Z1, X2, Y2, Z2):
    return math.sqrt((X1-X2)*(X1-X2)+\
                     (Y1-Y2)*(Y1-Y2)+\
                     (Z1-Z2)*(Z1-Z2))
def Distance(X1, Y1, X2, Y2):
    return math.sqrt((X1-X2)*(X1-X2)+(Y1-Y2)*(Y1-Y2))

# Helpers to access data in everscape.db

def Avatar_of_session(session_id):
# Extract array of all avatar in a session, this method is
# used a lot as the resulting array can convert "the 3rd
# avatar in session x" into "avatar no 5". The avatars id are
# not contiguous.
# The resulting array of id is ordered with ascending order.
    global sessions
    try:
        con = lite.connect("everscape.db")
        with con:
            cur = con.cursor()
            cur.execute("\
                SELECT DISTINCT avatar_no FROM Avatar\
                WHERE session_id = %d\
                ORDER BY avatar_no asc;\
            " % sessions[session_id])
            rows = cur.fetchall()
    except:
        print("error accessing database")
    result = []
    for row in rows:
        result.append(row[0])
    return result

def Trajectory_points(session_id, avatar_no, avatar_array = []):
# Return a list of lists. Each sublist is a point in the
# trajectory of an avatar: [[X, Y, Z, ts], [X, Y, Z, ts], ...]
    global sessions
    # avatar_array is a list of avatar ids in a session.
    if len(avatar_array) == 0:
        avatar_array = Avatar_of_session(session_id)
    try:
        #connect to database
        con = lite.connect('everscape.db')
        with con:
            cur = con.cursor()
            #ask for position and timestamp, order by time
            cur.execute("SELECT X, Y, Z, ts FROM Position\
                        WHERE session_id = %d AND\
                        avatar_no = %d\
                        ORDER BY ts asc;"\
                        % (sessions[session_id],\
                        avatar_array[avatar_no]))
            rows = cur.fetchall()
    except:
        print("error accessing database")
    return rows

def Trajectory(session_id, avatar_no, avatar_array = []):
# Returns a list containing the list of X positions, the list
# of Y positions, the list of Z positions, the list of
# timestamps of positions, for an avatar in a session.
    global sessions
    # avatar_array is a list of avatar ids in a session.
    if len(avatar_array) == 0:
        avatar_array = Avatar_of_session(session_id)
    try:
        #connect to database
        con = lite.connect('everscape.db')
        with con:
            cur = con.cursor()
            #ask for position and timestamp, order by time
            cur.execute("SELECT X, Y, Z, ts FROM Position\
                        WHERE session_id = %d AND\
                        avatar_no = %d\
                        ORDER BY ts asc;"\
                        % (sessions[session_id],\
                            avatar_array[avatar_no]))
            rows = cur.fetchall()
    except:
        print("error accessing database")
    X = []
    Y = []
    Z = []
    ts = []
    for row in rows:
    # remap the data to the good format
        X.append(row[0])
        Y.append(row[1])
        Z.append(row[2])
        ts.append(row[3])
    return [X, Y, Z, ts]


def TimeChoice(session_id):
# Returns a list containing the list of avatars in the
# session, the list of the time at which they respectively
# made a decision, the list of the decision they made.
# Can fail if the Time_Choice table was not built yet.
    global sessions
    try:
        #connect to database
        con = lite.connect('everscape.db')
        with con:
            cur = con.cursor()
            #ask for position and timestamp, order by time
            cur.execute("SELECT avatar_no, ts, choice\
                        FROM Time_Choice\
                        WHERE session_id = %d \
                        ORDER BY ts ASC;" % \
                        sessions[session_id]\
            )
            rows = cur.fetchall()
    except:
        print("error accessing database")
    avatars = []
    ts = []
    choices = []
    for row in rows:
    # remap data to good format
        avatars.append(row[0])
        ts.append(row[1])
        choices.append(row[2])
    return [avatars, ts, choices]

def x_series(session_id, avatar_no, avatar_array = []):
# Returns a list containing the list of X positions and the
# the list of the corresponding timestamps for an avatar in a
# session
    global sessions
    # avatar_array is a list of avatar ids in a session.
    if len(avatar_array) == 0:
        avatar_array = Avatar_of_session(session_id)
    con=lite.connect('everscape.db')
    with con:
        cur = con.cursor()
        cur.execute('\
            SELECT X, ts FROM Position\
            WHERE session_id = %d AND\
            avatar_no = %d\
            ORDER BY ts ASC;\
        ' % (sessions[session_id], avatar_array[avatar_no]))
        rows = cur.fetchall()
    X=[]
    T=[]
    for row in rows:
    # remap data to good format
        X.append(row[0])
        T.append(row[1])   
    return T, X

def diffX_hist(session_id, avatar_array = []):
# Speed on X axis, can be used to detect "teletransportation"
# of some users
# Returns the list of speeds
    global sessions
    # avatar_array is a list of avatar ids in a session.
    if len(avatar_array) == 0:
        avatar_array = Avatar_of_session(session_id)
    X=[]
    T=[]
    con=lite.connect('everscape.db')
    with con:
        cur = con.cursor()
        for avatar_no in avatars:
            cur.execute('\
                SELECT X, ts FROM Position\
                WHERE session_id = %d AND\
                avatar_no = %d\
                ORDER BY ts ASC;\
            ' % (sessions[session_id], avatar_array[avatar_no]))
            rows = cur.fetchall()
            mem_X = rows[0][0]
            mem_T = rows[0][1] - 1
            for row in rows:
                X.append((row[0] - mem_X)/(row[1] - mem_T))
                mem_X = row[0]
                mem_T = row[1]
    return X

def y_series(session_id, avatar_no, avatar_array = []):
# cf x_series
    global sessions
    # avatar_array is a list of avatar ids in a session.
    if len(avatar_array) == 0:
        avatar_array = Avatar_of_session(session_id)
    con=lite.connect('everscape.db')
    with con:
        cur = con.cursor()
        cur.execute('\
            SELECT Y, ts FROM Position\
            WHERE session_id = %d AND\
            avatar_no = %d\
            ORDER BY ts ASC;\
        ' % (sessions[session_id], avatar_array[avatar_no]))
        rows = cur.fetchall()
    Y=[]
    T=[]
    for row in rows:
    # remap data to good format
        Y.append(row[0])
        T.append(row[1])
    return T, Y

def diffY_hist(session_id, avatar_array = []):
#cf diffX_hist
    global sessions
    # avatar_array is a list of avatar ids in a session.
    if len(avatar_array) == 0:
        avatar_array = Avatar_of_session(session_id)
    Y=[]
    T=[]
    con=lite.connect('everscape.db')
    with con:
        cur = con.cursor()
        for avatar_no in avatars:
            cur.execute('\
                SELECT Y, ts FROM Position\
                WHERE session_id = %d AND\
                avatar_no = %d\
                ORDER BY ts ASC;\
            ' % (sessions[session_id], avatar_array[avatar_no]))
            rows = cur.fetchall()
            mem_Y = rows[0][0]
            mem_T = rows[0][1] - 1
            for row in rows:
                Y.append(float(row[0] - mem_Y)/\
                            float(row[1] - mem_T))
                mem_Y = row[0]
                mem_T = row[1]
    return Y

def z_series(session_id, avatar_no, avatar_array = []):
#cf x_series
    global sessions
    # avatar_array is a list of avatar ids in a session.
    if len(avatar_array) == 0:
        avatar_array = Avatar_of_session(session_id)
    con=lite.connect('everscape.db')
    with con:
        cur = con.cursor()
        cur.execute('\
            SELECT Z, ts FROM Position\
            WHERE session_id = %d AND\
            avatar_no = %d\
            ORDER BY ts ASC;\
        ' % (sessions[session_id], avatar_array[avatar_no]))
        rows = cur.fetchall()
    Z=[]
    T=[]
    for row in rows:
        Z.append(row[0])
        T.append(row[1])
    return T, Z

def diffZ_hist(session_id, avatar_array = []):
#cf diffX_hist
    global sessions
    # avatar_array is a list of avatar ids in a session.
    if len(avatar_array) == 0:
        avatar_array = Avatar_of_session(session_id)
    Z=[]
    T=[]
    con=lite.connect('everscape.db')
    with con:
        cur = con.cursor()
        for avatar_no in avatars:
            cur.execute('\
                SELECT Z, ts FROM Position\
                WHERE session_id = %d AND\
                avatar_no = %d\
                ORDER BY ts ASC;\
            ' % (sessions[session_id], avatar_array[avatar_no]))
            rows = cur.fetchall()
            mem_Z = rows[0][0]
            mem_T = rows[0][1] - 1
            for row in rows:
                Z.append(float(row[0] - mem_Z)/\
                            float(row[1] - mem_Tx))
                mem_Z = row[0]
                mem_T = row[1]
    return Z

def train_logs(session_id):
#returns train access logs as:
#   avatar asking for train, date of request, seat granted?
#not tested
    global sessions
    con = lite.connect('everscape.db')
    with con:
        cur = con.cursor()
        cur.execute('\
                    SELECT avatar_no, ts, granted_bool\
                    FROM ReplyTrainSeat\
                    WHERE session_id = %d\
                    ORDER BY ts ASC;' %\
                    sessions[session_id])
        rows = cur.fetchall()
    return rows

def info_session(session_id):
#returns info on session session:
#   length of session, nb of avatars
#time is in the format mmsscc, with cc the hundredth of seconds
    global sessions

    con = lite.connect('everscape.db')
    with con:
        cur = con.cursor()
        cur.execute('\
            SELECT length_sim, nb_participants\
            FROM \
                (SELECT session_id as id, MAX(ts) as length_sim\
                 FROM Position WHERE session_id = %d\
                 GROUP BY id)\
                    NATURAL JOIN\
                (SELECT session_id as id,\
                 COUNT(avatar_no) as nb_participants\
                 FROM Avatar WHERE session_id = %d\
                 GROUP BY id);\
        ' % (sessions[session_id], sessions[session_id]))
        rows = cur.fetchall()
    return rows

def requested_train(logs, avatar_id):
#returns true if the avatar has asked for a train seat
# Note that as we compare to the logs, avatar_id is the id of
# the avatar, not his number.
    # avatar_array is a list of avatar ids in a session.
    for log in logs:
        if log[0] == avatar_id:
            return True
    return False

def granted_train(logs, avatar_id):
#returns true if the avatar was granted a train seat
# Note that as we compare to the logs, avatar_id is the id of
# the avatar, not his number.
    for log in logs:
        if( log[0] == avatar_id and log[2] == 1):
            return True
    return False

def car_logs(session_id):
# returns car spawn logs as:
# avatar who took a car, date, true is after concert false 
# otherwise
    global sessions
    con = lite.connect('everscape.db')
    with con:
        cur = con.cursor()
        cur.execute('\
                    SELECT avatar_no, ts, after_before_bool\
                    FROM CarSpawns\
                    WHERE session_id = %d\
                    ORDER BY ts ASC;' %\
                    sessions[session_id])
        rows = cur.fetchall()
    return rows


def car_return(logs, avatar_id, avatar_array = []):
# True if the avatar returned by car
    # avatar_array is a list of avatar ids in a session.
    if len(avatar_array) == 0:
        avatar_array = Avatar_of_session(session_id)
    for log in logs:
        if log[0] == avatar_array[avatar_id] and log[2] == 1:
            return True
    return False

def car_after(session_id, avatar_no, avatar_array = []):
# Returns the time at which an avatar took the car on the way
# back. If he didn't take the car, returns -1. If he took more
# than one car, returns the time for the last one.
    global sessions
    # avatar_array is a list of avatar ids in a session.
    if len(avatar_array) == 0:
        avatar_array = Avatar_of_session(session_id)
    con = lite.connect('everscape.db')
    with con:
        cur = con.cursor()
        cur.execute('\
            SELECT ts FROM CarSpawns\
            WHERE session_id = %d\
            AND avatar_no = %d\
            AND after_before_bool = 1;'%\
            (sessions[session_id], avatar_array[avatar_no])\
        )
        rows = cur.fetchall()
    if len(rows) == 0:
        return -1
    elif len(rows) == 1:
        return rows[0][0]
    else :
        return rows[-1][0]

def car_before(session_id, avatar_no, avatar_array = []):
# Same as car_after but before concert
    global sessions
    # avatar_array is a list of avatar ids in a session.
    if len(avatar_array) == 0:
        avatar_array = Avatar_of_session(session_id)
    con = lite.connect('everscape.db')
    with con:
        cur = con.cursor()
        cur.execute('\
            SELECT ts FROM CarSpawns\
            WHERE session_id = %d\
            AND avatar_no = %d\
            AND after_before_bool = 0;'%\
            (sessions[session_id], avatar_array[avatar_no])\
        )
        rows = cur.fetchall()
    if len(rows) == 0:
        return -1
    elif len(rows) == 1:
        return rows[0][0]
    else :
        return rows[-1][0]

def earthquake_time(session_id):
# Returns the time at which the earthquake occurs
    global sessions
    con = lite.connect('everscape.db')
    with con:
        cur = con.cursor()
        cur.execute('\
             SELECT ts FROM Earthquake\
            WHERE session_id = %d\
            ;' % sessions[session_id]\
        )
        row = cur.fetchone()
    return row[0]

#-----------------------------------------------------
# Helpers to plot graphs, trajectories etc...

def Trajectory3D_plot(session_id, avatar_no):
# Plot 3D Trajectory from a player:
    data = Trajectory(session_id, avatar_no)
    X = data[0]
    Y = data[1]
    Z = data[2]
    C = []

    #color cycle params
    norm = len(X)
    freq = 2.0*math.pi/float(norm)
    for i in range(len(X)):
    # Uses a helper method to pick colors on a color disk at
    # regular phases.
    # The color of the points in the trajectory will shift
    # from blue to green to red as the avatar progresses.
        color = Color_cycle(i,freq)
        C.append(color)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(len(X)):
        ax.scatter(X[i], Y[i], Z[i], c=C[i], marker='o')

    plt.show()

def Trajectory2D_plot(session_id, avatar_no):
# Plot 2D Trajectory from a player:
    data = Trajectory(session_id, avatar_no)
    X = data[0]
    Y = data[1]

    plt.plot(X, Y, marker='o')

    plt.show()

def Trajectory2DTime_plot(session_id, avatar_no):
# Plot the trajectory of an avatar with color blue before he
# makes his choice of trajectory, with color red after.
# good for vizualizing the time of choice.
    avatars, ts, choices = TimeChoice(session_id)
    # avatars is the real id of the avatar, these ids doesn't
    # necessarily follow each other.
    if choices[avatar_no] == -1:
        choice_time = -1
        print(" Avatar didn't made a choice")
    else:
        choice_time = ts[avatar_no]
    data = Trajectory(session_id, avatar_no)
    X = data[0]
    Y = data[1]
    T = data[3]

    state = 0
    for i in range(len(X)):
        if T[i] == choice_time:
            state = 1
        if state == 0:
            plt.plot(X[i], Y[i], 'bs')
        else:
            plt.plot(X[i], Y[i], 'rs')
    plt.show()

def Trajectory2DTimeAll_plot(session_id):
# Plot all trajectories after the avatar performing the
# trajectory made a choice
    avatars, ts, choices = TimeChoice(session_id)
    # avatars is the real id of the avatar, these ids doesn't
    # necessarily follow each other.
    for avatar in avatars:
        avatar_index = avatars.index(avatar)
        if choices[avatar_index] == -1:
        # If the user didn't made a choice, no need to plot it
            continue
        choice_time = ts[avatar_index]
        data = Trajectory(session_id, avatar_index)
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
# Plot only the first point in trajectory after an avatar took
# a decision. Ideal to spot the place at which the avatar made
# a decision
    avatars, ts, choices = TimeChoice(session_id)
    # avatars is the real id of the avatar, these ids doesn't
    # necessarily follow each other.
    for avatar in avatars:
        avatar_index = avatars.index(avatar)
        choice_time = ts[avatar_index]
        data = Trajectory(session_id, avatar_index)
        X = data[0]
        Y = data[1]
        T = data[3]
        C = []
        norm = len(X)
        #color cycle params

        state = 0
        for i in range(norm):
            if  T[i] == choice_time:
                plt.plot(X[i], Y[i], 'b.')
    plt.show()

def Trajectories_plot(session_id, liminf=0, limsup='none'):
# Print trajectories for avatars between liminf and limsup.
# liminf and limsup doesn't refer to the id of avatars. For
# example the first avatar, even if his id is 34, will be
# referenced by 0. Hence, the method will plot a number of
# avatars equal to limsup - liminf.
    fig = plt.figure()
    avatar_array = Avatar_of_session(session_id)

    if type(limsup) is int and\
        limsup <= len(avatar_array) and\
        limsup >= liminf:
        avatar_array = avatar_array[liminf:limsup]

    C = []

    #color cycle params
    freq = 2.0*math.pi/float(len(avatar_array))
    for j in range(len(avatar_array)):
        color = Color_cycle(j,freq)
        C.append(color)

    ax = fig.add_subplot(111, projection='3d')

    for avatar_no in avatar_array:
        avatar_index = avatars.index(avatar)
        data = Trajectory(session_id, avatar_index)
        X = data[0]
        Y = data[1]
        Z = data[2]

        for i in range(len(X)):
            ax.scatter(X[i], Y[i], Z[i], c=C[avatar_index],\
                        marker='o')

    plt.show()

def Print_axis(session_id, avatar_no, axis='x'):
# Print the trajectory on only one axis for an avatar.
    if axis == 'x':
        data = x_series(session_id, avatar_no)
    elif axis == 'y':
        data = y_series(session_id, avatar_no)
    elif axis == 'z':
        data = z_series(session_id, avatar_no)
    else:
        print("axis can be 'x', 'y' or 'z' only")
        return

    plt.plot(data[0], data[1], linestyle="-")
    plt.show()

def Print_axis_all(session_id, axis='x', liminf=0, limsup='none'):
# cf Trajectories_plot. It's the same but only for one axis
    avatar_array = Avatar_of_session(session_id)
    C = []
    if type(limsup) is int and\
        limsup <= len(avatar_array) and\
        limsup >= liminf:
        avatar_array = avatar_array[liminf:limsup]

    #color cycle param
    freq = 2.0*math.pi/float(len(avatar_array))

    for i in range(len(avatar_array)):
    # A different color for each avatar
        color = Color_cycle(i, freq)
        C.append(color)

    for i in range(len(avatar_array)):
        if axis == 'x':
            data = x_series(session_id, i)
        elif axis == 'y':
            data = y_series(session_id, i)
        elif axis == 'z':
            data = z_series(session_id, i)
        else:
            print('axis can be x, y or z only')
            return
        plt.plot(data[0], data[1], c=C[i], linestyle="-")

    plt.show()

# Note that as we compare to the logs, avatar_id is the id of
# the avatar, not his number.
# Note that as we compare to the logs, avatar_id is the id of
# the avatar, not his number.
