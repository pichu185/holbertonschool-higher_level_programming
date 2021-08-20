#!/usr/bin/python3
'''Write a Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and displays the
body of the response (decoded in utf-8)
'''

import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    if sys.argv[1] and sys.argv[2]:
        data = urllib.parse.urlencode({'email': sys.argv[2]})
        data = data.encode('ascii')
        req = urllib.request.Request(sys.argv[1])
        with urllib.request.urlopen(req, data) as res:
            print(res.read().decode('utf-8'))
