#!/usr/bin/python3
'''
Write a Python script that fetches https://intranet.hbtn.io/status
'''
import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get(argv[1])
        if req.status_code < 400:
                print(req.text)
        else:
                print("Error code: {}".format(req.status_code))
