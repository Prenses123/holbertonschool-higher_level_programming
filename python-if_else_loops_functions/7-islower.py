#!/usr/bin/python3
def islower(c):
    i = ord(c)
    if 97 <= i <= 122:
        print("{} is lower".format(c))
        return True
    print("{} is upper".format(c))
    return False
