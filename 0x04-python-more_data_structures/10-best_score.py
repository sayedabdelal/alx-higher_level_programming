#!/usr/bin/python3
def best_score(a_dictionary):
    best_name_score = None
    id = 0

    if a_dictionary is None:
        return best_name_score

    for k, v in a_dictionary.items():
        if v > id:
            id = v
            best_name_score = k
    return best_name_score
