#!/usr/bin/python3
""" sends a POST request to the passed URL with the email as a parameter """
from urllib import request, parse
import sys


if __name__ == "__main__":
    req = parse.urlencode({'email': sys.argv[2]})
    req = req.encode('ascii')
    reqst = request.Request(sys.argv[1], req)
    with request.urlopen(reqst) as response:
        html = response.read()
        print(html.decode('utf-8'))
