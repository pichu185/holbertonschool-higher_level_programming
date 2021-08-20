#!/usr/bin/python3
'''Write a Python script that fetches https://intranet.hbtn.io/status'''

import urllib.request

if __name__ == "__main__":
	with urllib.request.urlopen("https://intranet.hbtn.io/status") as resp:
		html = resp.read()
		print("Body response:")
		print("\t- type:", type(html))
		print("\t- content:", html)
        print("\t- utf8 content:", html.decode('utf-8'))
