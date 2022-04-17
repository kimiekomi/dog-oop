#! /usr/bin/env python3

import time

debug = True
trace = True

class Timer:
    def __init__(self):
        if debug: print("constructed Timer class")

        self.start_time = None

    def start(self):
        if debug: print("called start()")

        if self.start_time != None:
            print("Timer already started")

        self.start_time = time.perf_counter()

        if trace: print(f"Start Time: {self.start_time:0.1f}")

    def stop(self):
        if debug: print("called stop()")

        if self.start_time == None:
            print("Timer has NOT started")

        self.stop_time = time.perf_counter()
        self.elapsed_time = self.stop_time - self.start_time

        self.start_time = None

        if trace: print(f"Elapsed Time: {self.elapsed_time:0.1f} seconds")


class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

        self.is_hungry = False
        self.is_tired = False
        self.is_bored = False

        timer = Timer()
        timer.start()

        print(f"Created {self.age} year old {self.breed} named {self.name}")

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
    dog = Dog("Lima", 2, "Malamute")