#!/usr/bin/python3
"""Write a Python script that fetches"""
import urllib.request
import urllib.error
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    request = urllib.request.Request(url=url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.status))