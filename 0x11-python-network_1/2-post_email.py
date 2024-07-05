#!/usr/bin/python3
"""Write a Python script that fetches"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    param = {"email": argv[2]}
    data = urllib.parse.urlencode(param).encode('utf-8')
    request = urllib.request.Request(url=url, data=data, method='post')
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))