#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
-Your script should take 4 arguments: mysql username, mysql password,
database name and state name searched (no argument validation needed)
-You must use the module MySQLdb (import MySQLdb)
-Your script should connect to a MySQL server running on localhost at port 3306
-You must use format to create the SQL query with the user input
-Results must be sorted in ascending order by states.id
-Results must be displayed as they are in the example below
-Your code should not be executed when imported
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                              passwd=argv[2], db=argv[3], port=3306,
                              charset="utf8")
	cursor = db.cursor()
	cursor.execute("SELECT * FROM states WHERE name = '{}'".format(argv[4]))
	querry = cursor.fetchall()
	for row in querry:
		if row[1] == argv[4]:
			print(row)
	db.close()
