#!/usr/bin/python3
"""This is a function."""


def write_file(filename="", text=""):
    """add"""
    with open(filename, "w+", encoding="utf-8") as f:
        f.write(text)
        print(f.read())
