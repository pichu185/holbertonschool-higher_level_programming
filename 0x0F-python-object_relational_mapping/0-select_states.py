#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa:
-Your script should take 3 arguments: mysql username, mysql password and
database name (no argument validation needed)
-You must use the module MySQLdb (import MySQLdb)
-Your script should connect to a MySQL server running on localhost at port 3306
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
    cursor.execute("SELECT * FROM states ORDER BY id")
    querry = cursor.fetchall()
    for row in querry:
        print(row)
    db.close()
