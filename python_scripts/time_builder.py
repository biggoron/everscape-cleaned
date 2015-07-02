import sqlite3 as lite
import sys
from dataset import *
from database_adapter import *
from exclusive_areas import *
from trajectory_plotting import *

con = lite.connect('everscape.db')
with con :
    cur = con.cursor()
    try:
        cur.execute("\
            DROP TABLE Time_choice2;\
        ")
        print("Database deleted")
    except:
        print("Still no Time_choice table to drop")

    cur.execute("\
        CREATE TABLE Time_choice2 (\
            session_id INTEGER,\
            avatar_no INTERGER,\
            mmss INTEGER,\
            choice INTEGER\
        );\
    ")

choice_hashes = {}
con = lite.connect('everscape.db')
with con :
    cur = con.cursor()
    cur.execute("\
        SELECT * FROM Path\
    ")
    rows = cur.fetchall()

print("choices imported")

for row in rows:
    try:
        choice_hashes[row[0]]
    except:
        choice_hashes[row[0]] = {}
    choice_hashes[row[0]][row[1]]=row[3]

print("choices hash constructed")


time_finder = TimeFinder()
print("tree constructed")

con = lite.connect('everscape.db')
with con :
    cur = con.cursor()
    for session in choice_hashes:
        print("Doing session %d" % session)
        if session == 14:
            continue
        session_id = dataset.a.index(session)
        avatars_choice = choice_hashes[session]
        for avatar in avatars_choice:
            print("Doing avatar %d" % avatar)
            if avatars_choice[avatar] == 0:
                continue
            try:
                time_choices =\
                    time_finder.time(session_id, avatar)
            except:
                print("avatar %d from session %d" %\
                    (avatar, session))
                print("made choice %d" % avatars_choice[avatar])
                sys.exit()

                
            for choice in time_choices:
                cur.execute("\
                    INSERT INTO Time_Choice2 VALUES \
                    (%d, %d, %d, %d);" % \
                    (   session,\
                        avatar,\
                        choice[0],\
                        choice[1]\
                    )\
                )

