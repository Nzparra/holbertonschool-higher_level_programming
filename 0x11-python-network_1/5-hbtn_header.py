#!/usr/bin/python3
""" sends a POST request to the passed URL with the email as a parameter """
import requests
import sys


if __name__ == "__main__":
    try:
        req = requests.get(sys.argv[1])
        print(req.headers['X-Request-Id'])
    except:
        pass
