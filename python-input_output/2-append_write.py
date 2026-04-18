#!/usr/bin/python3
"sdfsdfds"


def append_write(filename="", text=""):
    """salam"""
    with open(filename, "a+", encoding="utf-8") as f:
        return f.write(text)
