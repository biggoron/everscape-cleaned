import helpers as hp
import sqlite3 as lite

def inspect_choices():
    global sessions
    sessions = hp.sessions
    for session_index in range(len(sessions)):
    # Iterating over sessions
        avatar_index = 0
        for avatar in hp.Avatar_of_session(session_index):
        # Iterating over avatars
            con = lite.connect('everscape.db')
            with con:
            # Picking the road taken by the avatar in the
            # database
                cur = con.cursor()
                cur.execute("\
                    SELECT path_going, path_returning\
                    FROM Path\
                    WHERE session_id = %d AND\
                            avatar_no = %d\
                    " % (sessions[session_index], avatar)\
                )
                path = cur.fetchone()
            path_going = path[0]
            path_returning = path[1]
            # Displaying the stored path
            # 0 is no choice made
            # 1 is by car, on the shore side (right side)
            # 2 is by car, on the mountain side (left side)
            # 3 is by train, the road is straight
            print("Avatar %d of session %d went by %d,\
                    returned by %d" %(\
                        sessions[session_index],\
                        avatar,\
                        path_going,\
                        path_returning\
                    )\
                )
            input("Press key to plot traj")
            # Printing the trajectory.
            hp.Trajectory2D_plot(session_index, avatar_index)
            print("")
            avatar_index += 1
