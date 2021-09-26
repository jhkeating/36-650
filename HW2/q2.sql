drop table rdata;
create table rdata(
	id serial PRIMARY KEY,
	a TEXT UNIQUE NOT NULL CHECK (char_length(a)<6),
	b TEXT UNIQUE NOT NULL CHECK (char_length(b)<6),
	moment DATE DEFAULT '2020-01-01',
	x NUMERIC(5,2) CHECK (x>0)
);
