#!/usr/bin/python3
def best_score(a_dictionary):

    if not a_dictionary:
        return None
    i = 0
    for key in a_dictionary:
        if a_dictionary[key] > i:
            i = a_dictionary[key]
            bigger_key = key
    return bigger_key
