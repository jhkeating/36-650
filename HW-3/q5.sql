ALTER TABLE player_bios
	ADD COLUMN position text;
UPDATE player_bios p
	SET position = n.position 
	FROM new_table n
	WHERE p.id = n.player; 
SELECT (firstname,lastname,position) FROM player_bios 
	ORDER BY id ASC
	LIMIT 5;
		
