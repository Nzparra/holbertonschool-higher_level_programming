#!/usr/bin/python3
""" sends a POST request to the passed URL with the email as a parameter """
import requests
import sys


if __name__ == "__main__":
    dic = {'q': ""}
    try:
        dic['q'] = sys.argv[1]
    except:
        pass
    req = requests.post('http://0.0.0.0:5000/search_user', dic)
    try:
        jn = req.json()
        if not jn:
            print("No result")
        else:
            print("[{}] {}".format(jn.get('id'), jn.get('name')))
    except:
        print("Not a valid JSON")
