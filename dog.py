#! /usr/bin/env python3

debug = True
trace = True

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

        is_hungry = False
        is_tired = False
        is_bored = False

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


    def eat(self):
        if debug: print("called eat()")

        if self.is_hungry: 
            print("munch munch munch")


    def sleep(self):
        if debug: print("called sleep()")

        if self.is_tired: 
            print("zzz zzz zzz")


    def walk(self):
        if debug: print("called walk()")

        if self.is_bored: 
            print("trot trot trot")


if __name__ == "__main__":
    pass