#!/usr/bin/python3
"""
Write a script that lists all City objects from the database
hbtn_0e_101_usa
- Your script should take 3 arguments: mysql username, mysql
password and database name
- You must use the module SQLAlchemy
- Your script should connect to a MySQL server running on 
localhost at port 3306
- You must use only one query to the database
- You must use the state relationship to access to the State
 object linked to the City object
- Results must be sorted in ascending order by cities.id
- Results must be displayed as they are in the example below
- Your code should not be executed when imported
"""

import sqlalchemy
from sys import argv
from model_state import Base, State
from model_city import City
