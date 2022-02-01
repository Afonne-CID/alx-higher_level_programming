#!/usr/bin/python3
"""List 10 commits (from the most recent to oldest) of a given
    repository

    Usage:
        ./100-github_commits.py <repo name> <owner name>
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])

    commits = requests.get(url).json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
