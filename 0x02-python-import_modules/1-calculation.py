#!/usr/bin/python3
import calculator_1
def add(a, b):
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))

def sub(a, b):
    a = 10
    b = 5
    print("{} - {} = {}".format(a, b, sub(a, b)))

def mul(a, b):
    a = 10
    b = 5
    print("{} * {} = {}".format(a, b, mul(a, b)))

def div(a, b):
    a = 10
    b = 5
    print("{} / {} = {}".format(a, b, div(a, b)))

    if __name__ == "__main__":
        main()
