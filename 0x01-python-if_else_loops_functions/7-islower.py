#!/usr/bin/python3
def islower(c):
    islower = __import__('7-islower').islower
    if islower == True:
        print("islower(c) is {}".format("upper"))
    else:
        print("islower(c) is {}".format("lower"))
