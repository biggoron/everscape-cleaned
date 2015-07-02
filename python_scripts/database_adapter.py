import sqlite3 as lite
import dataset

#extract array containing X, Y, Z lists for an avatar in a session
def Trajectory_points(session_id, avatar_no):
    try:
        #connect to database
        con = lite.connect('everscape.db')
        with con:
            cur = con.cursor()
            #ask for position and timestamp, order by time
            cur.execute("SELECT X, Y, Z, mmss FROM Position\
                        WHERE session_id = %d AND\
                        avatar_no = %d\
                        ORDER BY mmss asc;" % (dataset.a[session_id], avatar_no))
            rows = cur.fetchall()
    except:
        print("error accessing database")
    return rows

def Trajectory(session_id, avatar_no):
    try:
        #connect to database
        con = lite.connect('everscape.db')
        with con:
            cur = con.cursor()
            #ask for position and timestamp, order by time
            cur.execute("SELECT X, Y, Z, mmss FROM Position\
                        WHERE session_id = %d AND\
                        avatar_no = %d\
                        ORDER BY mmss asc;" % (dataset.a[session_id], avatar_no))
            rows = cur.fetchall()
    except:
        print("error accessing database")
    X = []
    Y = []
    Z = []
    mmss = []
    for row in rows:
        X.append(row[0])
        Y.append(row[1])
        Z.append(row[2])
        mmss.append(row[3])
    return [X, Y, Z, mmss]

#extract array of all avatar in a session
def Avatar_of_session(session_id):
    try:
        con = lite.connect("everscape.db")
        with con:
            cur = con.cursor()
            cur.execute("\
                SELECT DISTINCT avatar_no FROM Avatar\
                WHERE session_id = %d\
                ORDER BY avatar_no asc;\
            " % dataset.a[session_id])
            rows = cur.fetchall()
    except:
        print("error accessing database")
    result = []
    for row in rows:
        result.append(row[0])
    return result


def TimeChoice(session_id):
    try:
        #connect to database
        con = lite.connect('everscape.db')
        with con:
            cur = con.cursor()
            #ask for position and timestamp, order by time
            cur.execute("SELECT avatar_no, mmss, choice\
                        FROM Time_Choice3\
                        WHERE session_id = %d \
                        ORDER BY mmss ASC;" % \
                        session_id\
            )
            rows = cur.fetchall()
    except:
        print("error accessing database")
    avatars = []
    mmss = []
    choices = []
    print(rows)
    for row in rows:
        avatars.append(row[0])
        mmss.append(row[1])
        choices.append(row[2])
    return [avatars, mmss, choices]

    
#array with time and x position
def x_series(session_id, avatar_no):
    con=lite.connect('everscape.db')
    with con:
        cur = con.cursor()
        cur.execute('\
            SELECT X, mmss FROM Position\
            WHERE session_id = %d AND\
            avatar_no = %d\
            ORDER BY mmss ASC;\
        ' % (dataset.a[session_id], avatar_no))
        rows = cur.fetchall()
    X=[]
    T=[]
    for row in rows:
        X.append(row[0])
        T.append(row[1])   
    return T, X

#speed on x axis, not tested, need to add time, better displayed as histogram
def diffX_hist(session_id):
    X=[]
    T=[]
    avatars = Avatar_of_session(session_id)
    con=lite.connect('everscape.db')
    with con:
        cur = con.cursor()
        for avatar_no in avatars:
            cur.execute('\
                SELECT X, mmss FROM Position\
                WHERE session_id = %d AND\
                avatar_no = %d\
                ORDER BY mmss ASC;\
            ' % (dataset.a[session_id], avatar_no))
            rows = cur.fetchall()
            mem_X = rows[0][0]
            mem_T = rows[0][1] - 1
            
            for row in rows:
                X.append((row[0] - mem_X)/(row[1] - mem_T))
                mem_X = row[0]
                mem_T = row[1]
    return X

#cf x_series
def y_series(session_id, avatar_no):
    con=lite.connect('everscape.db')
    with con:
        cur = con.cursor()
        cur.execute('\
            SELECT Y, mmss FROM Position\
            WHERE session_id = %d AND\
            avatar_no = %d\
            ORDER BY mmss ASC;\
        ' % (dataset.a[session_id], avatar_no))
        rows = cur.fetchall()
    Y=[]
    T=[]
    for row in rows:
        Y.append(row[0])
        T.append(row[1])   
    return T, Y

#cf diffX_hist
def diffY_hist(session_id):
    Y=[]
    T=[]
    avatars = Avatar_of_session(session_id)
    con=lite.connect('everscape.db')
    with con:
        cur = con.cursor()
        for avatar_no in avatars:
            cur.execute('\
                SELECT Y, mmss FROM Position\
                WHERE session_id = %d AND\
                avatar_no = %d\
                ORDER BY mmss ASC;\
            ' % (dataset.a[session_id], avatar_no))
            rows = cur.fetchall()
            mem_Y = rows[0][0]
            mem_T = rows[0][1] - 1
            
            for row in rows:
                Y.append((row[0] - mem_Y)/(row[1] - mem_T))
                mem_Y = row[0]
                mem_T = row[1]
    return Y

#cf x_series
def z_series(session_id, avatar_no):
    con=lite.connect('everscape.db')
    with con:
        cur = con.cursor()
        cur.execute('\
            SELECT Z, mmss FROM Position\
            WHERE session_id = %d AND\
            avatar_no = %d\
            ORDER BY mmss ASC;\
        ' % (dataset.a[session_id], avatar_no))
        rows = cur.fetchall()
    Z=[]
    T=[]
    for row in rows:
        Z.append(row[0])
        T.append(row[1])   
    return T, Z

#cf diffX_hist
def diffZ_hist(session_id):
    Z=[]
    T=[]
    avatars = Avatar_of_session(session_id)
    con=lite.connect('everscape.db')
    with con:
        cur = con.cursor()
        for avatar_no in avatars:
            cur.execute('\
                SELECT Z, mmss FROM Position\
                WHERE session_id = %d AND\
                avatar_no = %d\
                ORDER BY mmss ASC;\
            ' % (dataset.a[session_id], avatar_no))
            rows = cur.fetchall()
            mem_Z = rows[0][0]
            mem_T = rows[0][1] - 1
            
            for row in rows:
                Z.append((row[0] - mem_Z)/(row[1] - mem_T))
                mem_Z = row[0]
                mem_T = row[1]
    return Z

#returns train access logs as:
#   avatar asking for train, date of request, seat granted?
#not tested
def train_logs(session_id):
    con = lite.connect('everscape.db')
    with con:
        cur = con.cursor()
        cur.execute('\
                    SELECT avatar_no, mmss, granted_bool\
                    FROM ReplyTrainSeat\
                    WHERE session_id = %d\
                    ORDER BY mmss ASC;' %\
                    dataset.a[session_id])
        rows = cur.fetchall()
    return rows

#returns info on session session:
#   length of session, nb of avatars
#time is in the format mmsscc, with cc the hundredth of seconds
def info_session(session_id):
    con = lite.connect('everscape.db')
    with con:
        cur = con.cursor()
        cur.execute('\
            SELECT length_sim, nb_participants\
            FROM \
                (SELECT session_id as id, MAX(mmss) as length_sim\
                FROM Position WHERE session_id = %d\
                GROUP BY id)\
                    NATURAL JOIN\
                (SELECT session_id as id, COUNT(avatar_no) as nb_participants\
                FROM Avatar WHERE session_id = %d\
                GROUP BY id);\
        ' % (dataset.a[session_id], dataset.a[session_id]))
        rows = cur.fetchall()
    return rows

#returns true if the avatar has asked for a train seat
def requested_train(logs, avatar_id):
    for log in logs:
        if log[0] == avatar_id:
            return True
    return False

#returns true if the avatar was granted a train seat
def granted_train(logs, avatar_id):
    for log in logs:
        if( log[0] == avatar_id and log[2] == 1):
            return True
    return False

#returns car spawn logs as:
# avatar who took a car, date, true is after concert false otherwise
def car_logs(session_id):
    con = lite.connect('everscape.db')
    with con:
        cur = con.cursor()
        cur.execute('\
                    SELECT avatar_no, mmss, after_before_bool\
                    FROM CarSpawns\
                    WHERE session_id = %d\
                    ORDER BY mmss ASC;' %\
                    dataset.a[session_id])
        rows = cur.fetchall()
    return rows


#true if the avatar returned by car
def car_return(logs, avatar_id):
    for log in logs:
        if log[0] == avatar_id and log[2] == 1:
            return True
    return False

def car_after(session_id, avatar_no):
    con = lite.connect('everscape.db')
    with con:
        cur = con.cursor()
        cur.execute('\
            SELECT mmss FROM Car_after\
            WHERE session_id = %d\
            AND avatar_no = %d;'%\
            (dataset.a[session_id], avatar_no)\
        )
        rows = cur.fetchall()
    if len(rows) == 0:
        return -1
    elif len(rows) == 1:
        return rows[0][0]
    else :
        print('alert')
        return rows[-1][0]
    
def car_before(session_id, avatar_no):
    con = lite.connect('everscape.db')
    with con:
        cur = con.cursor()
        cur.execute('\
             SELECT mmss FROM Car_before\
            WHERE session_id = %d\
            AND avatar_no = %d;'%\
            (dataset.a[session_id], avatar_no)\
        )
        rows = cur.fetchall()
    if len(rows) == 0:
        return -1
    elif len(rows) == 1:
        return rows[0][0]
    else :
        print('alert')
        return rows[-1][0]
    
def earthquake_time(session_id):
    con = lite.connect('everscape.db')
    with con:
        cur = con.cursor()
        cur.execute('\
             SELECT mmss FROM Earthquake\
            WHERE session_id = %d\
            ;' % dataset.a[session_id]\
        )
        row = cur.fetchone()
    return row[0]

