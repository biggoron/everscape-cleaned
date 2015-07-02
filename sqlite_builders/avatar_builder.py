#!/usr/bin/python
# -*- coding: utf8 -*-

import sqlite3 as lite
import sys
import csv
from os import listdir
from os.path import isfile, join
from helpers import *

# This script populates the Avatar table in the database.
# The tuples are like:
# session_id, avatar_no, message?
#
# message? is 1 if the player sent chat messages, 0 otherwise

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
path_csv = data.path

# Memory to store who sent messages
message_hash = {}
# Memory to store 
avatars = []
# Memory to store 
avatar_hash = {}

token = 0
# Loop taking one file in four (one per session)
for s in csv_files:
    if token % 4 == 0:
        # s is the filename, Mydate builds a custom date
        # object from the timestamp at the beginning of s
        session_id = MyDate(s).session_id()
        message_hash[session_id] = set()
        # Concatenation of the path to csv, the timestamp of
        # session and the end of the filename to obtain a
        # given type of csv for a precise session 
        with open(path_csv + s[:14] + 'message.csv', mode='r')\
            as csvfile:
            reader = csv.reader(csvfile, delimiter=' ',\
                        quotechar='|')
            admin_token = 0
            for row in reader:
            # Examining the message log, keeping track of who
            # sent messages
                message_hash[session_id].add(\
                    # this is a helper function
                    number_from_name(row[0])\
                )
    token += 1

token = 0
for s in csv_files:
# Same kind of loop, this time on the log of positions for
# avatars.
    if token % 4 == 0:
        # s is the filename, Mydate builds a custom date
        # object from the timestamp at the beginning of s
        session_id = MyDate(s).session_id()
        avatar_hash[session_id] = set()
        # Concatenation of the path to csv, the timestamp of
        # session and the end of the filename to obtain a
        # given type of csv for a precise session 
        with open(path_csv + s[:14] + 'avatar.csv', mode='r') \
        as csvfile:
        # Examining the position log, keeping track of
        # distinct avatars   

            reader = csv.reader(csvfile, delimiter=',',\
                quotechar='|')
            for row in reader:
                avatar_hash[session_id].add(\
                    # this is a helper function
                    number_from_name(row[5])\
                )
    token += 1

con = lite.connect('everscape.db')
with con:
#store in database
    # Clean table
    cur = con.cursor()
    cur.execute("\
        DELETE FROM Avatar;\
    ")

    for session_id in avatar_hash:
    # Iterating over the avatars of each session to build the 
    # tuples to be inserted in the database.
        avatar_set = avatar_hash[session_id]

        #Set operation & (intersection) - (exclusion)
        in_message_set = avatar_set & message_hash[session_id]
        not_message_set = avatar_set - in_message_set

        for no in in_message_set:
            cur.execute("\
                INSERT INTO Avatar VALUES(%d, %d, %d)\
                " % ( \
                        session_id,\
                        no, \
                        1))
        for no in not_message_set:
            cur.execute("INSERT INTO Avatar VALUES\
                        (%d, %d, %d)" % ( \
                        session_id,\
                        no, \
                        0))
