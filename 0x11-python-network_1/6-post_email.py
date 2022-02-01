#!/usr/bin/python3
""" Send parameters in a `POST` request to a given URL.

    Usasge:
        ./6-post-email.py <URL> <email>
    Return:
        Displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    input_url = sys.argv[1]
    email = {"email": sys.argv[2]}

    value = requests.post(input_url, data=email)
    print(value.text)
