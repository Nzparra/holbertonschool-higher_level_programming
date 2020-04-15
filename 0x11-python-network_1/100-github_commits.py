#!/usr/bin/python3
""" sends a POST request to the passed URL with the email as a parameter """
from requests import get
import sys


if __name__ == "__main__":
    try:
        user = sys.argv[1]
        rep = sys.argv[2]
        url = "https://api.github.com/repos/{}/{}/commits".format(user, rep)
        req = get(url).json()
        for i in range(0, 10):
            print("{}: {}".format(req[i].get('sha'), req[i].get('commit')
                                  .get('author').get('name')))
    except:
        pass
