#!/usr/bin/python3
"""List 10 commits (from the most recent to oldest) of a given
    repository
"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    repo = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(username, repo)

    commits = (requests.get(url)).json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
