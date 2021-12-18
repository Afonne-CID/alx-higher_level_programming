#!/usr/bin/python3
""" Prints the first `State` object from the database `hbtn_0e_6_usa \
        using sqlalchemy
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

    if (session.query(State).order_by(State.id).first()):
        state = session.query(State).order_by(State.id).first()
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    session.close()
