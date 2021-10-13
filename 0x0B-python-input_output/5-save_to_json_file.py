#!/usr/bin/python3
"""Defines a function that writes an Object to a text file
using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file using a JSON representation

    Args:
        my_obj (any type): Object to write to file
        filename: name to save file to
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
