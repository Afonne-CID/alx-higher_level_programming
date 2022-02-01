#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response
    (decoded in utf-8)
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    input_url = sys.argv[1]

    request = urllib.request.Request(input_url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
