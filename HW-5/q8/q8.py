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

def dummy(r):
	# returns r rows of dummy records
	result = ""
	for i in range(r):
		id = i+1
		first = "firstname" 
		last = "lastname"
		result +=  "("+str(id)+",'"+first+"','"+last+"'),"
	return result[:-1]

y = "INSERT INTO employees (id,fname,lname) VALUES "+dummy(500)

cur.execute(y)
cur.execute("SELECT * FROM employees LIMIT 10")

print("Employees table:")
employeeRows = cur.fetchall()
for row in employeeRows:
	print (row)

cur.close()
conn.close()

