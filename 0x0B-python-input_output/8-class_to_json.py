#!/usr/bin/python3
"""Defines a function that returns the dictionary description with
simple data structure (list, dictionary, string, integer and
boolean) for JSON serialization of an object
"""


def class_to_json(obj):
    """Returns objct (instance of a class) to json"""
    return obj.__dict__
