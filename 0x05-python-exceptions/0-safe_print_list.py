#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for y in range(x):
            i += 1
            print(f"{my_list[y]}", end="")
    except (IndexError):
        return i
    else:
        return x
    finally:
        print()
