import sqlite3 as lite
import csv
from os import listdir
from os.path import isfile, join

class MyDate:
#wrapper for dates
#extract info from YYMMDD_HHMMSS timestamps
    year = -1
    month = -1
    day = -1
    hour = -1
    minute = -1
    second = -1

    def to_string(self):
        return  '' + year + month + day +\
                '_' + hour + minute + second + '_'
    def year(self):
        return year
    def month(self):
        return month
    def day(self):
        return day
    def hour(self):
        return hour
    def minute(self):
         return minute
    def second(self):
         return second
    def __init__(self, date_string):
        self.year = int(date_string[:2])
        self.month = int(date_string[2:4])
        self.day = int(date_string[4:6])
        self.hour = int(date_string[7:9])
        self.minute = int(date_string[9:11])
        self.second = int(date_string[11:13])
    def date_list(self):
        return [self.year, self.month, self.day,\
                self.hour, self.minute, self.second]

    def session_id(self):
    # Finds in the database the session that was run at
    # that date. Returns -1 if no or more than one session
    # were found (one and only one is expected)

    # Note: You need to run session_builder.py before running
    # this method, as you need to have the data loaded in
    # the session table of the database
        try:
            con = lite.connect('everscape.db')
            with con:
                cur = con.cursor()
                cur.execute("\
                        SELECT DISTINCT id FROM Session WHERE \
                            year = %d AND \
                            month = %d AND \
                            day = %d AND \
                            hour = %d AND \
                            minute = %d AND \
                            second = %d" %\
                        (\
                        self.year,\
                        self.month,\
                        self.day, \
                        self.hour, \
                        self.minute, \
                        self.second)\
                        )
                rows = cur.fetchall()
                if len(rows) != 1:
                    raise Exception()
                else:
                    return rows[0][0]
        except Exception as inst:
            print("found more than one session id for the date")
            return -1

    def id_to_date(id):
    # Finds the date of a given session 
        try:
            con = lite.connect('everscape.db')
            with con:
                cur = con.cursor()
                cur.execute("SELECT year, month, day,\
                                hour, minute, second \
                        FROM Session WHERE id = %d" % id)
                rows = cur.fetchall()
                if len(row) == 1:
                    row = rows[0]
                    return MyDate(row[0], row[1], row[2],\
                                row[3], row[4], row[5])
                else:
                    raise exception
        except Exception as inst:
           print("No session found! ")
           return MyDate(0,0,0,0,0,0)

class Position:
#wrapper for positions
    car = 0
    X = 0
    Y = 0
    Z = 0
    R = 0
    ts = 0

    def car(self):
        return self.car
    def X(self):
        return self.X
    def Y(self):
        return self.Y
    def Z(self):
        return self.Z
    def R(self):
         return self.R
    def ts(self):
        return self.ts
    def __init__(self, car, X, Y, Z, R,\
                ts, session_min, session_sec):
        self.car = car
        self.X = X
        self.Y = Y
        self.Z = Z
        self.R = R
        self.ts = ts_builder(ts, session_min, session_sec)

def ts_builder(ts, session_min, session_sec):
        position_min = int(ts[14:16]) - session_min
        if (position_min < 0):
            position_min += 60
        position_sec = int(ts[17:19]) - session_sec
        position_centi = int(ts[20:22])
        if (position_sec < 0):
            position_sec += 60
            position_min -= 1
        return ((60 * position_min) + position_sec) * 100 + position_centi

class CSVData:
# Path to csv files
    path = ''
    # List of files
    collection = []
    # Number of files
    nb_files = 0
    # Number of sessions (nb_files / 4)
    nb_sessions = 0
    # Is the data reliable ( %4 == 0 )
    valid = False
    # Contains the csv files and associated method that are
    # used in the scripts that build the database

    # Default is that the files are in csv_everscape directory
    def __init__(self, path_csv="./csv_everscape/"):
        #list of the csv files, l is the number of files
        files = [f for f in listdir(path_csv) if \
                            isfile(join(path_csv, f)) ]
        # As the names of the files begin with the timestamp,
        # doing so will order the session by date, from the
        # older to the newer.
        files.sort()

        self.collection = files
        nb = self.collection.__len__()

        #each session has 4 files hence a valid dataset has a
        #number of file that is multiple of 4
        if nb % 4 == 0:
            self.nb_files = nb
            self.nb_sessions = int(nb / 4)
            self.path = path_csv
            self.valid = True
        else:
            self.valid = False

def number_from_name(name):
    if (name[-2:] == "in")\
    or (name[-2:] == "er"):
    # When a admin send a message, instead of
    # having an id, the player is referenced by
    # "Admin", or "AdminPlayer". I associate an id
    # of 101 to such players (only one per
    # session)
        cur_avatar = 101
    elif name[-2] == "t":
    # if the id take only on number, the log of
    # the player will be "participant3" instead of
    # "participant03". Hence, if the penultimate
    # caracter in the string is t instead of a
    # number, only the ultimate caracter is stored
    # as the player id.
        cur_avatar = int(name[-1])
    else:
    # Normal case where the two last caracters in
    # the log are the id of the player.
        cur_avatar = int(name[-2:])
    return cur_avatar


class StringParser:
    def player_str(big_string):
            player_part = big_string.split('|')[0]
            return number_from_name(player_part)

    def granted_str(big_string):
            granted_part = big_string.split(' ')[-1]
            if granted_part != '-1':
                return 1
            else:
                return 0
