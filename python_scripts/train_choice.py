import sqlite3 as lite
from database_adapter import *
import dataset

con = lite.connect('everscape.db')
with con :
    cur = con.cursor()
#    Create an empty table to host train logs
    cur.execute("\
        DROP TABLE Train;\
    ")
    cur.execute("\
        CREATE TABLE Train (\
            session_id INTEGER,\
            avatar_no INTEGER,\
            mmss INTEGER,\
            PRIMARY KEY (session_id, avatar_no, mmss)\
            );\
    ")


for session_id in dataset.a:
    logs = train_logs(session_id)
    con = lite.connect('everscape.db')
    with con:
        cur = con.cursor()
        for log in logs:
            cur.execute("\
                INSERT INTO Train VALUES\
                (%d, %d, %d);"\
                %(\
                    session_id,\
                    log[0],\
                    log[1]\
                )\
            )
