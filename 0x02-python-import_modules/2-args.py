#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv) - 1
    if argc == 0:
        print("0 argument.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))
    for j in range (1, argc + 1):
        print("{}: {}".format(j, sys.argv[j]))
