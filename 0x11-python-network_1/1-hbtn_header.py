#!/usr/bin/python3
"""Sends a request to a supplied URL and displays `X-Request-Id` variable
    found in the header
"""
import sys
import urllib.request


if __name__ == "__main__":
    input_url = sys.argv[1]

    request = urllib.request.Request(input_url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
