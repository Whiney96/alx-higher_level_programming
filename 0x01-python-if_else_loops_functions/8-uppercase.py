#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if str.islower():
            print("{0:C}".format(i))
