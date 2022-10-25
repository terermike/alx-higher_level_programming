#!/usr/bin/python3
""" json to object"""
import json


def from_json_string(my_str):
    """ eturns an object (Python data structure) represented
    by a JSON string"""
    return json.loads(my_str)
