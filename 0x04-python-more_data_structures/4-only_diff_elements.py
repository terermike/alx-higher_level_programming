#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    z = set_1.difference(set_2)
    x = set_2.difference(set_1)
    z.update(x)
    return z
