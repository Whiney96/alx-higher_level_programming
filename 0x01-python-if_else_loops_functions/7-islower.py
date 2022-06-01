#!/usr/bin/python3
def islower(c):
    islower = __import__('7-islower').islower

    if c is True:
        print(c, " is {}".format("upper"))
    else:
        print(c, " is {}".format("lower"))
