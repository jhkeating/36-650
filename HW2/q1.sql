create table rdata(
	id serial PRIMARY KEY,
	a TEXT CHECK (char_length(a)<6),
	b TEXT CHECK (char_length(b)<6),
	moment DATE,
	x NUMERIC(5,2)
);
