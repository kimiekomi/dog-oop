#! /usr/bin/env python3

debug = True
trace = True

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, new_name):
        self.name = new_name

    @property
    def age(self):
        return self.age

    @age.setter
    def name(self, new_age):
        self.name = new_age

    @property
    def breed(self):
        return self.breed

    @breed.setter
    def name(self, new_breed):
        self.name = new_breed


if __name__ == "__main__":
    pass