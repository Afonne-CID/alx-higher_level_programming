#!/usr/bin/python3
""" Lists all State objects, and corresponding City objects contained\
        in the database `hbtn_0e_101_usa

    Usage: ./100-relationship_states_cities_list.py\
            <mysql username>\
            <mysql passwd>\
            <mysql db>\

    Ex Output:
        <state id>: <state name>
        <tabulation><city id>: <stiy name>
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State)\
            .order_by(State.id):
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
