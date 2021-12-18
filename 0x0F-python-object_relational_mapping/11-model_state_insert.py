#!/usr/bin/python3
""" Adds the State object "Louisiana" to the dataase `hbtn_0e_6_usa`
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    new = State(name="Louisiana")
    session.add(new)
    session.commit()
    print(new.id)
