#!/usr/bin/python3
def multiple_returns(sentence):
    le_n = len(sentence)
    if le_n == 0:
        fst = "None"
    else:
        fst = sentence[0]
    mult = (le_n, fst)
    return (mult)
