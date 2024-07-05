#!/usr/bin/python3
"""Write a Python script that fetches"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url=url)
    if response.status_code < 400:
        print(response.text)
    else:
        print("Error code: {}".format(response.status_code))