#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    mmeli = 0

    for m in  range(0, x):
        try:
            print(f"{my_list[m]}", end="")
            mmeli += 1
        except IndexError:
            break
        print()
        return (mmeli)
