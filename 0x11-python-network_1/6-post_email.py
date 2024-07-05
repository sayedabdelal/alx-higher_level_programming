#!/usr/bin/python3
"""Write a Python script that fetches"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    data = {"email": argv[2]}
    response = requests.post(url=url, data=data)
    print(response.text)