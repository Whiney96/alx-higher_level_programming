#!/usr/bin/python3
def add(a, b):
    a = 1
    b = 2
    x = a + b
    print("{0} + {1} = {2}".format(a, b, x))

    if __name__ == "__main__":
        import sys
        add(int(sys.argv[2]))
