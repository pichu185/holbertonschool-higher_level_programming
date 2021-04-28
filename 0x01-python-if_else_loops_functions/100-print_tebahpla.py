#!/usr/bin/python3
for j in range(ord('Z'), ord('A')-1, -1):
    if j % 2 == 0:
        j = j + 32
    print("{:c}".format(j), end='')
