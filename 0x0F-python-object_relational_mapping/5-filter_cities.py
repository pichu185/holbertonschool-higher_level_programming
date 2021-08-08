#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
- Your script should take 4 arguments: mysql username, mysql password,
database name and state name (SQL injection free!)
- You must use the module MySQLdb (import MySQLdb)
- Your script should connect to a MySQL server running
 on localhost at port 3306
- Results must be sorted in ascending order by cities.id
- You can use only execute() once
- The results must be displayed as they are in the example below
- Your code should not be executed when imported
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                              passwd=argv[2], db=argv[3], port=3306,
                              charset="utf8")
	cursor = db.cursor()
	cursor.execute("SELECT cities.name FROM cities INNER JOIN states\
        ON cities.state_id = states.id WHERE states.name = %s", (argv[4],))
	querry = cursor.fetchall()
	if len(querry) == 0:
		print('')
	for i in range(len(querry)):
		if i != (len(querry) - 1):
			print("{}, ".format(querry[i][0]), end="")
		else:
			print(querry[i][0])
	db.close()
