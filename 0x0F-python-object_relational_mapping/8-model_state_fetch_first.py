#!/usr/bin/python3
"""
Write a script that prints the first State object from
the database hbtn_0e_6_usa
- Your script should take 3 arguments: mysql username,
 mysql password and database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state - from 
model_state import Base, State
- Your script should connect to a MySQL server running on 
localhost at port 3306
- The state you display must be the first in states.id
- You are not allowed to fetch all states from the database 
before displaying the result
- The results must be displayed as they are in the example below
- If the table states is empty, print Nothing followed by a new line
- Your code should not be executed when imported
"""

import sqlalchemy
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = sqlalchemy.create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
        )
    Base.metadata.create_all(engine)
    session = sqlalchemy.orm.Session(engine)
    try:
        print("{}: {}".format(
            session.query(State).order_by(State.id).first().id,
            session.query(State).order_by(State.id).first().name
            )
        )
    except:
        print('Nothing')
    session.close()
    