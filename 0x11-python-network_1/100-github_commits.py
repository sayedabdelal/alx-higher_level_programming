#!/usr/bin/python3
"""Write a Python script that fetches"""
import requests
from sys import argv

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) == 2:
        data = {'q': argv[1]}
    else:
        data = {'q': ""}
    response = requests.post(url=url, data=data)
    try:
        resp = response.json()
        if resp:
            print("[{}] {}".format(resp.get("id"), resp.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")