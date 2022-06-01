#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if str == 65:
            print("{0:c}".format(i))
        elif str < 91:
            print("{0:c}".format(i))
