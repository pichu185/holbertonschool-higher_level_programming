#!/usr/bin/python3
"""
Write a script that lists all State objects, and corresponding City
objects, contained in the database hbtn_0e_101_usa
- Your script should take 3 arguments: mysql username, mysql 
password and database name
- You must use the module SQLAlchemy
- The connection to your MySQL server must be to localhost on port 3306
- You must only use one query to the database
- You must use the cities relationship for all State objects
- Results must be sorted in ascending order by states.id and cities.id
- Results must be displayed as they are in the example below
- Your code should not be executed when imported
"""

import sqlalchemy
from sys import argv
from model_state import Base, State
from model_city import City
