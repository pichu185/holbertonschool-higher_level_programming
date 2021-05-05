#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argc = sys.argv
    if len(argc) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argc[1])
    b = int(argc[3])

    if argc[2] == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))

    elif argc[2] == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))

    elif argc[2] == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))

    elif argc[2] == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
