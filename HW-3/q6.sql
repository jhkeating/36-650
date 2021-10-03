ALTER TABLE player_bios
	ADD COLUMN height_updated numeric;
UPDATE player_bios
	SET height_updated=12*split_part(height,'-',1)::integer+split_part(height,'-',2)::integer;
ALTER TABLE player_bios
	DROP COLUMN height;
ALTER TABLE player_bios
	RENAME COLUMN height_updated to height;
SELECT (firstname,lastname,height) from player_bios
	ORDER BY id ASC
	LIMIT 5; 
