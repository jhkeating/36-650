import subprocess
import sys
import psycopg2

conn = psycopg2.connect(host="localhost", 
                        port="7890", 
                        user="postgres", 
                        password="mysecretpassword", 
                        database="postgres")

cur = conn.cursor()

x = "CREATE TABLE employees(id serial,fname varchar(10),lname varchar(10))"

cur.execute(x)
cur.execute("SELECT * FROM employees")

print("Employees table:")
for row in cur:
	print (row)

cur.close()
conn.close()
