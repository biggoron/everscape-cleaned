import sqlite3 as lite
from database_adapter import *
import dataset

#this script stores the times at which people take cars to go to concert and to come back

con = lite.connect('everscape.db')
with con :
    cur = con.cursor()
#    Create an empty tables to host car logs
    cur.execute("\
        DROP TABLE Car_before;\
    ")
    cur.execute("\
        DROP TABLE Car_after;\
    ")
    cur.execute("\
        CREATE TABLE Car_before (\
            session_id INTEGER,\
            avatar_no INTEGER,\
            mmss INTEGER,\
            PRIMARY KEY (session_id, avatar_no, mmss)\
            );\
    ")
    cur.execute("\
        CREATE TABLE Car_after (\
            session_id INTEGER,\
            avatar_no INTEGER,\
            mmss INTEGER,\
            PRIMARY KEY (session_id, avatar_no, mmss)\
            );\
    ")

#iterates over sessions
for session_id in dataset.a:
    #gets the logs from cars
    logs = car_logs(session_id)
    con = lite.connect('everscape.db')
    with con:
        cur = con.cursor ()
        for log in logs:
            if log[2] :
                cur.execute("\
                    INSERT INTO Car_after VALUES\
                    (%d, %d, %d);"\
                    %(\
                        session_id,\
                        log[0],\
                        log[1]\
                    )\
                )
            else:
                cur.execute("\
                    INSERT INTO Car_before VALUES\
                    (%d, %d, %d);"\
                    %(\
                        session_id,\
                        log[0],\
                        log[1]\
                    )\
                )

