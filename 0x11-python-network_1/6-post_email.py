#!/usr/bin/python3
""" Send parameters in a `POST` request to a given URL.

    Usasge:
        ./2-post-email.py <URL> <email>
    Return:
        Displays the body of the response (decoded in utf-8)
"""
import sys
import requests


if __name__ == "__main__":
    input_url = sys.argv[1]
    email = {"email": sys.argv[2]}

    value = requests.post(url, data=email)
    print(value.text)
