#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = [(new.append(replace) if x == search else new.append(x))for x in my_list]
    return new
