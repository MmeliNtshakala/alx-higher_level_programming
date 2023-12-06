#!/usr/bin/python3

def best_score(a_dictionary):
    best_score = 0
    best_score1 = None
    if a_dictionary:
        for x, y in a_dictionary.items():
            if x > best_score:
                best_score = x
                best_score1 = y
        return best_score1
    else:
        return None
