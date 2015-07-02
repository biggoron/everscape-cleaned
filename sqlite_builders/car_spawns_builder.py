#!/usr/bin/python
# -*- coding: utf8 -*-

import sqlite3 as lite
import sys
import csv
from os import listdir
from os.path import isfile, join
from helpers import *
from helpers import StringParser as sp

# csv files
# files are already sorted by date of simulation
data = CSVData()
if not data.valid:
# exit if nb of files not divisible by 4
    print("csv files are not divisible by 4")
    sys.exit(1)
csv_files = data.collection
l = data.nb_files
path_csv = data.path

con = lite.connect('everscape.db')
with con:
    cur = con.cursor()
    #Clear corresponding tables in database
    cur.execute("\
        DELETE FROM Earthquake;"\
    )
    cur.execute("\
        DELETE FROM CarSpawns;"\
    )
    cur.execute("\
        DELETE FROM OnBridgeCrossed;"\
    )
    cur.execute("\
        DELETE FROM OnBridgeTouched;"\
    )
    cur.execute("\
        DELETE FROM ReplyHelicopter;"\
    )
    cur.execute("\
        DELETE FROM ReplyTrainSeat;"\
    )

# diverse memories to store data before putting it into
# database
token = 0
cur_avatar = 0
avatar_hash = {}
bridge_touch_memory = 0
bridge_cross_memory = 0
train_hash = {}
helicopter_hash = {}
earthquake_token = 0

for s in csv_files:
# enumerates the logs in log files, session by session, and
# insert into database events like car_spawns, train logs or
# earthquake logs.
    if token % 4 == 0:
        # getting the session_id
        session_id = MyDate(s).session_id()

        con = lite.connect('everscape.db')
        with con:
            cur = con.cursor()
            # Time of session in minutes and seconds
            minute = int(s[9:11])
            second = int(s[11:13])
            # Used to see if we are before or after earthquake
            earthquake_token = 0
            # Used to see if the earthquake happens during the
            # concert.
            concert_token = 0
            with open(path_csv + s[:14] + 'log.csv', mode='r')\
            as csvfile:
                reader = csv.reader(csvfile, delimiter=',',\
                                    quotechar='|')
                counter = 0
                for i in range(102):
                # memories
                    avatar_hash[i] = 0
                    train_hash[i] = 0
                    helicopter_hash[i] = 0
                for row in reader:
                    if row[1] == "OnForceAssistConcert":
                    # detects concert
                        concert_token = 1
                    if row[1] == "OnEarthquakeStarted" and\
                    concert_token == 1:
                    # The log is for an earthquake, happening
                    # during or after concert
                        earthquake_token = 1
                        ts = ts_builder(row[0], minute, second)
                        cur.execute("INSERT INTO Earthquake\
                                    VALUES (%d, %d);"\
                                    %(session_id, ts)\
                        )

                    if row[1] == "RequestCarSpawnPoint":
                    # A car has been picked up
                        ts = ts_builder(row[0], minute, second)
                        cur_avatar = sp.player_str(row[2])
                    if avatar_hash[cur_avatar] != ts:
                    # such conditions are used to erase
                    # duplicates in the original data
                        cur.execute('INSERT INTO CarSpawns\
                        VALUES (%d, %d, %d, %d)' % ( \
                                    session_id, \
                                    earthquake_token, \
                                    ts, \
                                    cur_avatar))
                    # we take into memory the car spawn
                    # because there can be some duplicates.
                    avatar_hash[cur_avatar] = ts
                    if row[1] == "OnBridgeCrossed":
                        ts = ts_builder(row[0], minute, second)
                        if bridge_cross_memory != ts:
                            cur.execute('INSERT INTO\
                                OnBridgeCrossed VALUES \
                                        (%d, %d)' % ( \
                                        session_id, \
                                        ts))
                        # memory to avoid duplicates
                        bridge_cross_memory =  ts
                    if row[1] == "OnBridgeTouched":
                        ts = ts_builder(row[0], minute, second)
                        if bridge_touch_memory != ts:
                            cur.execute('INSERT INTO\
                            OnBridgeTouched VALUES \
                                            (%d, %d)' % ( \
                                        session_id, \
                                        ts))
                        # memory to avoid duplicates
                        bridge_touch_memory =  ts
                    if row[1] == "RequestHelicopterSeat":
                        ts = ts_builder(row[0], minute, second)
                        cur_avatar = sp.player_str(row[2])
                        granted = sp.granted_str(row[2])
                        if helicopter_hash[cur_avatar] != 1:
                            cur.execute('INSERT INTO\
                            ReplyHelicopter VALUES \
                                        (%d, %d, %d, %d)' % ( \
                                        session_id, \
                                        ts, \
                                        cur_avatar, \
                                        granted))
                        # memory to avoid duplicates
                        helicopter_hash[cur_avatar] = 1
                    if row[1] == "ReplyTrainSeat":
                        ts = ts_builder(row[0], minute, second)
                        cur_avatar = sp.player_str(row[2])
                        granted = sp.granted_str(row[2])
                        if train_hash[cur_avatar] != ts:
                            cur.execute('INSERT INTO\
                            ReplyTrainSeat VALUES\
                                        (%d, %d, %d, %d)' % ( \
                                        session_id, \
                                        ts, \
                                        cur_avatar, \
                                        granted))
                        # memory to avoid duplicates
                        train_hash[cur_avatar] = ts
                if earthquake_token == 0:
                # If no earthquake during concert has been
                # detected fill up the earthquake table with a -1.
                    cur.execute("INSERT INTO Earthquake\
                                    VALUES (%d, %d);"\
                                    % (session_id, -1)\
                    )
        # go to next csv file
    token += 1
