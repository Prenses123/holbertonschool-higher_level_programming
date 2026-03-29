#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary.update({key: value})
    for i in a_dictionary.keys():
        print(f"{i}: {a_dictionary[i]}")
