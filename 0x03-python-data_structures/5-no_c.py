#!/usr/bin/python3
def no_c(my_string):
    for x in my_string:
        if x == 'c':
            return my_string.remove('c')
        elif x == 'C':
            return my_string.remove('C')
        else:
            return my_string[:]
