#!/usr/bin/python3
def uniq_add(my_list=[]):
    b = []
    for i in my_list:
        if b.count(i) == 0:
            b.append(i)
    return sum(b)
