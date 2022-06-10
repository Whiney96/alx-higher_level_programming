#!/usr/bin/python3
def search_replace(my_list, search, replace):
    a = 'search'
    b = 'replace'
    return (list(lambda x, b, a: a if x == b else x) for x in my_list)
