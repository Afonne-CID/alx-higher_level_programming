#!/usr/bin/python3
""" Lists all City objects contained in the database `hbtn_0e_101_usa

    Usage: ./102-relationship_cities_states_list.py\
            <mysql username>\
            <mysql passwd>\
            <mysql db>\

    Ex Output:
        <city id>: <city name> -> <state name>
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

    for city in session.query(City)\
            .order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
