#!/usr/bin/python3
""" sends a POST request to the passed URL with the email as a parameter """
from requests import get, auth
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = sys.argv[1]
    pasw = sys.argv[2]
    req = get(url, auth=auth.HTTPBasicAuth(user, pasw))
    print(req.json().get('id'))
