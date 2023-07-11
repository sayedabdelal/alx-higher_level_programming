#!/usr/bin/python3
"""This module defines a JSON file-writing fun"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file"""
    with open(filename, "r") as f:
        return json.dump(f)
