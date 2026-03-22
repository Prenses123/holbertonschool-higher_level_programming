#!/usr/bin/python3
def multiple_returns(sentence):
    a = list(sentence)
    return len(sentence), a[0] if len(a) > 0 else None