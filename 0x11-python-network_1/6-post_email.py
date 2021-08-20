#!/usr/bin/python3
'''
Write a Python script that fetches https://intranet.hbtn.io/status
'''
import requests
from sys import argv

if __name__ == "__main__":
    mail = {'email': argv[2]}
    req = requests.post(argv[1], data=mail)
    print(req.text)
