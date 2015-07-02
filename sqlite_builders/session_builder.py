#!/usr/bin/python
# -*- coding: utf8 -*-

import sqlite3 as lite
import sys
from helpers import MyDate, CSVData

# This script insert tuples like:
# session_id, year, month, day, hour, minute, second
# in the session table.
#
# Session_id is obtained by ordering the sessions by date.
# The date of the session is obtained thanks to the timestamp
# prefixing the name of csv files

# csv files
# files are already sorted by date of simulation
data = CSVData()
if not data.valid:
# exit if nb of files not divisible by 4
    print("csv files are not divisible by 4")
    sys.exit(1)
csv_files = data.collection
l = data.nb_files
n = data.nb_sessions

#list of the sessions to be inserted in database
sessions = []
for i in range(n):
    #insert the id of session in the list
    sessions.append([i])


#loop taking one file in four
#each turn in loop adds time information to a session
token = 0
for s in csv_files:
    if token % 4 == 0:
        # s is the filename, Mydate builds a custom date
        # object from the timestamp at the beginning of s
        session_date = MyDate(s)

        # this line add the time related fields to the session
        # tuples to be inserted in database
        sessions[int(token/4)].extend(session_date.date_list())
    token += 1


# Inserts the tuples from sessions list into the session table
# in database.
con = lite.connect('everscape.db')
with con:

    # Cleans database
    cur = con.cursor()
    cur.execute("\
        DELETE FROM Session;\
    ")
    # Insert values
    cur.executemany("\
        INSERT INTO Session VALUES(?,?,?,?,?,?,?);\
    ", sessions)
