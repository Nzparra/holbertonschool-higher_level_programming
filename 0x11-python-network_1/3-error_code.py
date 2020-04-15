#!/usr/bin/python3
""" sends a POST request to the passed URL with the email as a parameter """
from urllib import request, error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except error.HTTPError as fail:
        print('Error code: {}'.format(fail.code))
