#!/usr/bin/python3
def uniq_add(my_list=[]):
    set(my_list)
    for x in my_list:
        result = x + x
        print("Result: {:d}".format(result))
