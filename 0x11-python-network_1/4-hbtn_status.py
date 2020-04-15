#!/usr/bin/python3
""" sends a POST request to the passed URL with the email as a parameter """
import requests


if __name__ == "__main__":
    req = requests.get('https://intranet.hbtn.io/status')
    req = req.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.
          format(type(req), req))
