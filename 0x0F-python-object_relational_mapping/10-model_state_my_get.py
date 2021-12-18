#!/usr/bin/python3
""" Prints `State` object with the name passed as argument \
        from the database `hbtn_0e_6_usa, using sqlalchemy
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    status = False
    for state in session.query(State).order_by(State.id):
        if state.name == sys.argv[4]:
            status = True
            print("{}".format(state.id))
    if (not status):
        print("Not found")

    session.close()
