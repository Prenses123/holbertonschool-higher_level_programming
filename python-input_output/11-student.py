#!/usr/bin/python3
"sdfsdfds"
import json


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            new_dict = {}
            for i in attrs:
                if isinstance(i, str) and i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for i in json.keys():
            self.__dict__[i] = json[i]
        return self.__dict__
