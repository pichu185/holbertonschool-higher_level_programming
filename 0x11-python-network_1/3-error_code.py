#!/usr/bin/python3
'''sends a request to the URL and displays the body of the response'''

import urllib.request
import urllib.error
from sys import argv

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
