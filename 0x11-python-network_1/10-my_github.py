#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id"""

import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == '__main__':
    res = requests.get('https://api.github.com/user',
                        auth=HTTPBasicAuth(argv[1], argv[2]))
    if res.status_code == 200:
        dictionary = res.json()
        print(dictionary['id'])
    else:
        print(None)
