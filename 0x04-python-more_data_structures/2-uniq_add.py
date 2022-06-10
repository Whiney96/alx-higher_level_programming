#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set(my_list)
    result = map(lambda x: x+x, uniq)
    print("Result: {:d}".format(result))
