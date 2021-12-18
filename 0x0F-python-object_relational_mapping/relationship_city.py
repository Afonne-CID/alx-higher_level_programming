#!/usr/bin/python3
""" Defines a class `City`
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base, State


class City(Base):
    """ Represents a 'city table' for a MySQL database \
            and inherits from the `Base` class

    __tablename__(str): Name of MySQL table to create, in this case `city`
    id (sqlalchemy.Integer): `state` id
    name (sqlalchemy.String): `state` name
    """
    __tablename__ = "cities"

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement=True)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer,
                      ForeignKey("states.id"),
                      nullable=False)
