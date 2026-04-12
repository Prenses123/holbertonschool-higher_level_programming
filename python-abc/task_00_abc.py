#!/usr/bin/python3
"my module"
from abc import ABC,abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound():
        pass
class Dog(Animal):
    def sound():
        print(f"Bark")
class Cat(Animal):
    def sound():
        print(f"Meow")
