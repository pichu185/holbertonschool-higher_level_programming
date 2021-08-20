#!/usr/bin/python3
'''
Write a Python script that fetches https://intranet.hbtn.io/status
'''
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        dict = req.json()
        if len(dict.keys()) > 0:
            print("[{}] {}".format(dict.get('id'), dict.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
