#!/usr/bin/python3

def search_replace(my_list, search, replace):
    replace_list = my_list[:]
    for x in range(len(replace_list)):
        if replace_list[x] == search:
            replace_list[x] = replace

    return replace_list
