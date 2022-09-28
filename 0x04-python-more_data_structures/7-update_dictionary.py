#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    x = a_dictionary.setdefault(key, value)
    return x
