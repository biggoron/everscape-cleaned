The files in this folder build some extra features and store
them in the database.

First helpers.py give access to many accessors to database and
helper function. 

Then path_builder.py analyses the trajectory of each avatar to
extract which road the avatar took (ie: Car by the shore, car
by the mountain, train), then store this feature in database

Then, given the path of each avatar,
threaded_exclusive_zone.py provides a classifier able to
extract the time at which an avatar choose its road. The basic
principle is to find all neighbouring points from trajectories
of other avatars. If all the avatars that have been close to
the considered point are all from the same path than the
currently looked avatar, then this avatar has already chosen
its way. Else, not yet. The point of the algorithm is just to
find the transition.
As the computing is slow (querying many many times a KDTree
with a huge amount of points in it for a lot of neighbours),
the classifier can be called in parallel.

Finally threaded_time_builder.py calls the classifier from
threaded_exclusive_zone.py in a parallel way to find the time
of decision of each avatar that made a choice for each
session.
Attention: the computing for all the sessions take around 15
minutes running on 32 subprocess for a i7 processor. Be prepared to
wait.
