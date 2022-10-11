#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
    except IndexError:
        return i
    else:
        return x
    finally:
        print(" ")
