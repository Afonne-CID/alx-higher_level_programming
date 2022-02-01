#!/usr/bin/python3
"""Fetches `https://intranet.hbtn.io/status` using the `request` package
"""
import requests


if __name__ == "__main__":
    value = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(value.text)))
    print("\t- content: {}".format(value.text))
