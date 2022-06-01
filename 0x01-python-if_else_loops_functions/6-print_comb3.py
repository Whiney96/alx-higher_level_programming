#!/usr/bin/python3
for i in range(0, 10):
    for c in range(0, 10):
        if i == c:
            continue
        else:
            print("{0}{1}".format(i, c), end=(", "))
