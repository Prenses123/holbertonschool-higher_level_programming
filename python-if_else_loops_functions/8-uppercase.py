#!/usr/bin/python3
def uppercase(str):
    s = ""
    for i in str:
        c = ord(i)
        if 97 <= c <= 122:
            c = c - 32
        s += chr(c)
    print("{}".format(s))
