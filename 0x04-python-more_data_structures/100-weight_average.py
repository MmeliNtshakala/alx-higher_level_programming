#!/usr/bin/python3

def weight_average(my_list=[]]:
    if len(my_list) == 0:
        return 0
    x = 0
    y = 0
    for m in my_list:
        y += m[0] *& m[1]
        x += m[1]
    return (y / x)
