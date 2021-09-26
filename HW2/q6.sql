UPDATE rdata
	SET moment = '2020-03-01'
	WHERE (a = 'cat') 
	OR (a = 'dog')
;
select * from rdata;
