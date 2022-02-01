#!/usr/bin/python3
"""Sends a request to a URL and displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    input_url = sys.argv[1]

    value = requests.get(input_url)
    if (value.status_code >= 400):
        print("Error code: {}".format(value.status_code))
    else:
        print(value.text)
