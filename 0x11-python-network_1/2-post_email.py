#!/usr/bin/python3
""" Send parameters in a `POST` request to a given URL.

    Usasge:
        ./2-post-email.py <URL> <email>
    Return:
        Displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    input_url = sys.argv[1]
    email = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(email).encode("ascii")

    request = urllib.request.Request(input_url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
