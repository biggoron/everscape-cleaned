import sqlite3 as lite
# Note that we use only INTEGERs, even for ts timestamps
# The only exception is for X,Y,Z,R, the coordinates and
# rotation parameters of the points in the trajectories.
# After having work with the data it happened that when
# leaving the concert a full unit in distance is a too gross
# to analyse the data.

# Tables to be defined
tables = ['Session', 'Avatar', 'Position', 'OnBridgeTouched',\
            'OnBridgeCrossed', 'ReplyHelicopter',\
            'ReplyTrainSeat', 'CarSpawns', 'Earthquake']

con = lite.connect('everscape.db')
with con :
# Builds the squeleton of the database
    cur = con.cursor()
    for table in tables:
    # Remove table if present, catch exception if not
        try:
        # Try to drop table
            cur.execute("\
                DROP TABLE %s;\
            " % table )
        except:
        # Failing to drop table occurs and is due to a missing table.
            print("Table %s was not in database. Could not be dropped." % table)

    cur.execute(\
        "PRAGMA foreign_keys = true;"\
    )
    cur.execute(\
    #Create table Session
    """
        CREATE TABLE Session (
                id INTEGER PRIMARY KEY,
                year INTEGER,
                month INTEGER,
                day INTEGER,
                hour INTEGER,
                minute INTEGER,
                second INTEGER
                );
    """)

    cur.execute(\
    #Create table Avatar
    """
        CREATE TABLE Avatar (
                session_id INTEGER REFERENCES Session(id),
                avatar_no INTEGER,
                message_bool INTEGER,
                PRIMARY KEY (session_id, avatar_no)
                )
        ;
    """)

    cur.execute(\
    #Create table CarSpawns
    """
        CREATE TABLE CarSpawns (
                session_id INTEGER REFERENCES Session(id),
                after_before_bool INTEGER,
                ts INTEGER,
                avatar_no INTEGER REFERENCES Avatar(avatar_no),
                PRIMARY KEY (session_id, avatar_no, ts)
                )
        ;
    """)

    cur.execute(\
    #Create table Position
    """
        CREATE TABLE Position (
                session_id INTEGER REFERENCES Session(id),
                avatar_no INTEGER REFERENCES Avatar(avatar_no),
                ts INTEGER,
                X REAL,
                Y REAL,
                Z REAL,
                R REAL,
                car_bool INTEGER,
                PRIMARY KEY (session_id, avatar_no, ts, car_bool)
                )
        ;
    """)

    cur.execute(\
    #Create table OnBridgeTouched
    """
        CREATE TABLE OnBridgeTouched (
                session_id INTEGER REFERENCES Session(id),
                ts INTEGER,
                PRIMARY KEY (session_id, ts)
                )
        ;
    """)

    cur.execute(\
    #Create table OnBridgeCrossed
    """
        CREATE TABLE OnBridgeCrossed (
                session_id INTEGER REFERENCES Session(id),
                ts INTEGER,
                PRIMARY KEY (session_id, ts))
        ;
    """)

    cur.execute(\
    #Create table ReplyHelicopter
    """
        CREATE TABLE ReplyHelicopter (
                session_id INTEGER REFERENCES Session(id),
                ts INTEGER,
                avatar_no INTEGER REFERENCES Avatar(avatar_no),
                granted_bool INTEGER,
                PRIMARY KEY (session_id, ts, avatar_no))
        ;
    """)

    cur.execute(\
    #Create table ReplyTrainSeat
    """
        CREATE TABLE ReplyTrainSeat (
                session_id INTEGER REFERENCES Session(id),
                ts INTEGER,
                avatar_no INTEGER REFERENCES Avatar(avatar_no),
                granted_bool INTEGER,
                PRIMARY KEY (session_id, ts, avatar_no)
                )
        ;
    """)
    cur.execute(\
    #Create table ReplyTrainSeat
    """
        CREATE TABLE Earthquake (
                session_id INTEGER REFERENCES Session(id),
                ts INTEGER,
                PRIMARY KEY (session_id, ts)
                )
        ;
    """)
