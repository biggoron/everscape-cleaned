############################## Situation ################
Original data in sql script everscape.sql script
 -> Deletes root user
 -> need a client/server infrastructure: painfull for Data
 	Analysis
 -> Once the database is built, if modification are done, it is
 	difficult to share database
 -> Plenty of useless and redundant data

 => Transform data in a more usefull way, prone to agile
 	analysis. I choose to export interesting data to csv,
    planning to build a sqlite database from those csv.
#########################################################

---------------------------------------------------------
 -> I separated the everscape.sql script into little, unitary,
    error-less scripts, separated 
    logging-zagreb (everscape-zagreb.sql),
    logging (everscape-logging.sql),
    logging-everscape (everscape-everscape.sql). I dropped
    the configuration tables.

 -> Only logging-everscape is uselfull, I concentrated the
    effort on this one.

 -> deleted useless tables (blank, irrelevant contents). It 
    yields everscape-work.sql (this .sql file still contains
    plenty of useless data, but is roughly ok)
    HENCE, BUILDING THE DATABASE USE ONLY everscape-work.sql

 -> exported to csv the columns to be used into csv_everscape,
	thanks to csv1.sql

 -> used python scripts to import these csv into a normalized
 	sqlite table: easy to share, modify script. (in sqlite
			builders)

 ~> mysql data was highly redundant (id for lines, but same
	data), usefull data was sparse, not normalized, not
 	consistent (data found under different names),
 	experiments and real data were mixed
---------------------------------------------------------

 FORMAT OF THE .sql files.

 I will describe only the interesting tables in
 everscape-work.sql:

    First there is a collection of tables which names match:
    YYMMDD_HHMMSS_AvatarEntity
    These tables list the points in the trajectories of the
    avatars. Hence there is various fields like Positions on
    X, Y and Z axis, timestamp, id of the avatar etc...

    Then tables which names match:
    YYMMDD_HHMMSS_CarEntity
    These tables are just like the AvatarEntity tables but or
    when the user is in a car.

    Then tables which names match:
    YYMMDD_HHMMSS_ChatMessageEvent
    These tables are logs of the messages sent via the chat
    room

    Finally tables which names match:
    YYMMDD_HHMMSS_NetworkEvent or YYMMDD_HHMMSS_LogEvent 
    these tables have the same function and store the logs
    of various events in the simulation. For example 
    earthquake starting, departure of the train etc...

There is also many other table, but as they contain only a
timestamp and an id there is no way to understand their
purpose.
-----------------------------------------------------------
CSV FILES

csv_exporter.sql is a mysql bash script which select relevant
informations in the 4 types of tables described above and
store it in csv files.
As the mysql database contains 4 tables per session (one for
each type described above), I created 4 csv files per session
named like:
YYMMDD_HHMMSS_[Avatar|Car|Message|Log].csv
Looking at the first 4 SELECT operation in csv_exporter.sql
(#1 - 130212_141126) will show you the fields stored in the csv
Each "#x - YYMMDD_HHMMSS" paragraph in the scripts performs
the necessary actions to export data for the simultation
session that happened on the timestamp YYMMDD_HHMMSS.

This steps yields the csv files for 23 sessions (112 files)
-----------------------------------------------------------

ATTENTION: sql data files are not maintained on git: too heavy
