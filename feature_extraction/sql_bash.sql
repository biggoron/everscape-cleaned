-- This sql script selects the length of simulation, the number of participants,
-- and the date for each session in the database.
-- It was used to select the sessions taken into account into the analysis.
-- The array of the sessions used  in the analysis can be found at the top
-- of the helper file.
SELECT Session.id, length_sim, nb_participants, year, month, day
	FROM Session NATURAL JOIN ( 

		(SELECT session_id as id, MAX(mmss) as length_sim 
		FROM Position GROUP BY id) 	 
		NATURAL JOIN
		(SELECT session_id as id, COUNT(avatar_no) as nb_participants
		FROM Avatar GROUP BY id)
		)

	WHERE year = 14 AND nb_participants > 20
	ORDER BY Session.id asc;
