#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operators = ["+", "-", "*", "/"]
    if sys.argv[2] == operators[0]:
        print("{} + {} = {}".format(sys.argv[1], sys.argv[3], add(a, b)))
    elif sys.argv[2] == operators[1]:
        print("{} - {} = {}".format(sys.argv[1], sys.argv[3], sub(a, b)))
    elif sys.argv[2] == operators[2]:
        print("{} * {} = {}".format(sys.argv[1], sys.argv[3], mul(a, b)))
    elif sys.argv[2] == operators[3]:
        print("{} / {} = {}".format(sys.argv[1], sys.argv[3], div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
