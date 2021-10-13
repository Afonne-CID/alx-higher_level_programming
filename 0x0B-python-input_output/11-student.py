#!/usr/bin/python3
"""Defines a Student class
"""


class Student:
    """A class representing a student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation

        Args:
            first_name (str): Student's first name
            last_name (str): Student's last name
            age (int): Student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representationn of a Student

        If ``attrs`` is a list of strings, only attribute names contained
        in this list must be retrieved. If not indicated, all attributes
        must be retrived.

        Args:
            attrs (list): Indicates specific attributes to represent
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributs of the Student instance

        Args:
            json (dict): key will be public attribute name
                         value will be the value of the public attribute
        """
        for i, j in json.items():
            setattr(self, i, j)
