CREATE TABLE new_table(
	player integer references more_player_stats,
	prl numeric,
	position text);
INSERT INTO new_table (player,prl) (
	SELECT 
		id,
		round(per-67*va/(gp*minutes),1) 
	FROM more_player_stats);
UPDATE new_table
	set position='PF' 
	where prl>=11.3;
UPDATE new_table
	set position='PG' 
	where prl>=10.8 
	and prl<11.3;
UPDATE new_table
	set position='C' 
	where prl>=10.6 
	and prl<10.8;
UPDATE new_table
	set position='SG/SF' 
	where prl<10.6;
SELECT * from new_table 
	ORDER BY player ASC
	LIMIT 10;

