#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    """program that prints the number of and the list of its arguments."""
    num = len(sys.argv) - 1
    if num == 0:
        print("0 arguments.")
    elif num == 1:
        print("1 arguent:")
    else:
        print("{:d} arguments:".format(num))
    for i in range(1, num + 1):
        print('{:d}: {}'.format(i, sys.argv[i]))
