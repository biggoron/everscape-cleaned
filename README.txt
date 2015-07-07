EVERSCAPE PROJECT
-- Maintained on git under the name everscape-cleaned --
-- attention, sql data files are not maintained (too heavy) --
-------------------------------------------------------------------------------

The aims of this part of the project is:

    Understand the data,
    Migrate it to sqlite for easier use,
    Tidy it up,
    Document it,
    Apply datamining techniques on it to make its main interest apparent
-------------------------------------------------------------------------------

The project folder contains subfolders, grouping files by function:

    mysql_data/ contains the raw data from the experiment, a script to export it
    to csv files, the exported csv files and a README file documenting the 
    content of the .sql original files and the content of the exported csv files.
    The commentaries in the export script should be enough to understand the
    exportation.

    sqlite_builders/ contains a copy of the exported csv, python scripts to build a
    normalized database from the mysql dataset and some documentation for the
    resulting sqlite database. The commentaries in the python scripts should be
    enough to understand each one of them. A README file summarizes the purpose of
    each one of the scripts.

    feature_extraction/ contains all the scripts necessary to extract relevant
    features in the data and store them in the database, the hence completed
    database and a README file to summarize the purpose of each one of the scripts.

    data_analysis/ contains all the scripts used to visualize and  analyse the data 
    in the database containing the extracted features, and a README file summarizing
    the purpose of each one of the scripts. 

    python_scripts contains all the scripts that were written to understand, modify
    and analyse the data during the research process. Most of them are commented
    enough to understand them at first glance. A README file summarizes the
    purpose of each one of the scripts.
    This folder is here only to give a complete overview on the work done on
    everscape.

    visualization/ contains all the scripts used to visualize data. (usefull for 
    testing). You will also find a file documenting these scripts.

    Finally, resources/ contains all the figures obtained from scripts, further
    explanations on the overall process and possible continuations for the
    project
-------------------------------------------------------------------------------

The analysis of the data is able to extract the correlation between the choices
of the users with a precision fine enough to discriminate the play sessions that
were done "for real" and the ones that were done to test the software or to
play. We can notice a higher correlation in the sessions done "for real", as if
the stress of the moment lead people to have more gregarian behaviors. It is 
a very interesting result as it justifies that research on simulated data have
a meaning and that simulation can recreate at least part of the behaviour
expected from a dataset extracetd from real life.

The next steps in the project would be:

    To relaunch experiments to gather more data, in order to get more advanced
    results on it.

    To push further the automation and the generalization of the feature
    extracting and analysis scripts, in order to make a program able to
    automatically convert trajectories into a proper datastructure for analysis.
    For example, to understand the influence of preceding users' choices on the
    choices of the users behind, the series of position of users doesn't give
    much help. Still, after clustering trajectories and identifing  the
    "crossroad" points, a program can represent the trajectories by a graph in
    which the nodes contains informations on the choices made by users and the
    edges information on the paths taken by the users.
    The information about precise movements seconds by seconds is then
    abstracted to global paths and choices of paths.
    You will find more details on this possible continuation for the project in
    the resources/ directory

-------------------------------------------------------------------------------

 *The original file is kept on a server by the lab. Still be carefull with this
 .sql file, as loading it will alter your sql configuration (among other
 things destroy the root account to the sql server, which can be annoying...)
 If you are considering using the raw sql file, you should use the one present
 in this folder (everscape-work.sql), as I cleaned it to keep only the data, removing all the 
 mysql configuration related part.



Dan.
