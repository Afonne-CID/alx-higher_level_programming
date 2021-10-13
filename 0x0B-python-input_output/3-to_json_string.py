#!/usr/bin/python3
"""Defines a function that returns the JSON of a string"""
import json


def to_json_string(my_obj):
    """"Retuns the JSON representation of a string"""
    return json.dumps(my_obj)
