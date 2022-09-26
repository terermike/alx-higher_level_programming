#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = len(tuple_a)
    b = len(tuple_b)

    if tuple_a and tuple_b:
        if a >= 2 and b >= 2:
            return tuple((tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]))
        elif a < 1 and b >= 2:
            return tuple((tuple_a[0] + tuple_b[0], tuple_b[1]))
        elif b < 2 and a >= 2:
            return tuple((tuple_a[0] + tuple_b[0], tuple_a[1]))
        else:
            return tuple((tuple_a[0] + tuple_b[0], 0))
    elif tuple_a:
        return tuple((tuple_a[0], tuple_a[1]))
    else:
        return tuple((tuple_a[1], tuple_a[1]))
