#!/usr/bin/python
# -*- coding: utf8 -*-

import sqlite3 as lite
import sys
import csv
from os import listdir
from os.path import isfile, join
from helpers import MyDate, Position, CSVData

# csv files
# files are already sorted by date of simulation
data = CSVData()
if not data.valid:
# exit if nb of files not divisible by 4
    print("csv files are not divisible by 4")
    sys.exit(1)
path_csv = data.path
csv_files = data.collection
l = data.nb_files

con = lite.connect('everscape.db')
with con:
    cur = con.cursor()
    # Clear table in database
    cur.execute("\
        DELETE FROM Position;\
    ")

token = 0
cur_avatar = 0
avatar_hash = {}
for s in csv_files:
# exploring the logs session by session.
    if token % 4 == 0:
    # The loop is over the sessions. each session has 4 files.
    # hence the loop is skipped 3 times in 4
        # getting the session_id thanks to the timestamp in
        # the name of the file.
        session_id = MyDate(s).session_id()
        con = lite.connect('everscape.db')
        with con:
            cur = con.cursor()

            # Time of session in minutes and seconds
            minute = int(s[9:11])
            second = int(s[11:13])
            # Taking the logs line by line then storing them
            # in the new database. The time is taken as
            # relative to the beginning of the session, in
            # seconds. There can be multiple positions at a
            # single time in the original data, this case is
            # handled.
            with open(path_csv + s[:14] + 'avatar.csv', mode='r')\
            as csvfile:
                reader = csv.reader(csvfile, delimiter=',',\
                quotechar='|')
                counter = 0
                for i in range(102):
                # store the time of last log for each avatar
                    avatar_hash[i] = 0
                for row in reader:
                # enumerates the lines in the log
                    # converts the log into a position object
                    # the Position class is in a helper file
                    # during the conversion the time becomes
                    # relative.
                    position = Position(0, float(row[1]),\
                                float(row[2]), float(row[3]),\
                                float(row[4]), row[0],\
                                minute, second)
                    # tricky, one user don't have a name like
                    # participant12, but instead Admin or
                    # AdminUser. This part handles this case
                    if (row[5][-2:] == "in")\
                                or (row[5][-2:] == "er"):
                        cur_avatar = 101
                    elif row[5][-2] == "t":
                        cur_avatar = int(row[5][-1])
                    else:
                        cur_avatar = int(row[5][-2:])
                    # Try to insert the data in the database. 
                    ts = position.ts
                    # This condition ensure that if an
                    # avatar has two positions at the same
                    # date we insert only one position.
                    # Date is a primary key
                    if avatar_hash[cur_avatar] != ts:
                        cur.execute('INSERT INTO Position\
                        VALUES (%d, %d, %d, %f, %f,\
                                %f, %f, %d)' % ( \
                                    session_id, \
                                    cur_avatar, \
                                    ts, \
                                    position.X, \
                                    position.Y, \
                                    position.Z, \
                                    position.R, \
                                    position.car))
                    avatar_hash[cur_avatar] = ts

            # below is the same but for trajectories by car.
            avatar_hash = {}
            for i in range(102):
                avatar_hash[i] = 0
            with open(path_csv + s[:14] + 'car.csv', mode='r')\
            as csvfile:
                reader = csv.reader(csvfile, delimiter=',',\
                                    quotechar='|')
                for row in reader:
                    position = Position(1, float(row[1]),\
                            float(row[2]), float(row[3]),\
                            float(row[4]), row[0],\
                            minute, second)
                    if (row[5][-2:] == "in") or (row[5][-2:] == "er"):
                        cur_avatar = 101
                    elif row[5][-2] == "t":
                        cur_avatar = int(row[5][-1])
                    else:
                        cur_avatar = int(row[5][-2:])
                    ts = position.ts
                    if avatar_hash[cur_avatar] != ts:
                        cur.execute('INSERT INTO Position\
                        VALUES (%d, %d, %d, %d, %d,\
                                %d, %d, %d)' % ( \
                                    session_id, \
                                    cur_avatar, \
                                    position.ts, \
                                    position.X, \
                                    position.Y, \
                                    position.Z, \
                                    position.R, \
                                    position.car))
                    avatar_hash[cur_avatar] = ts
    token += 1
