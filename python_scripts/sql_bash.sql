
-- 2 -- Selects the date and nb of participants for all session ids
--SELECT * FROM Session INNER JOIN (SELECT session_id, COUNT(avatar_no) as
--	nb_participants FROM Avatar GROUP BY session_id) 
--	ON session_id = id ORDER BY id asc;

-- 3 -- Same with length of simulation
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
