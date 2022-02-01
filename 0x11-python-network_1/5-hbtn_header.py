#!/usr/bin/python3
"""Sends a request to a supplied URL and displays `X-Request-Id` variable
    found in the header using the `requests` package
"""
import sys
import requests


if __name__ == "__main__":
    input_url = sys.argv[1]

    value = requests.get(input_url)
    print(value.headers.get("X-Request-Id"))
