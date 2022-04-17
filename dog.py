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
        self._name = name
        self._age = age
        self._breed = breed

        self.is_hungry = False
        self.is_tired = False
        self.is_bored = False

        timer = Timer()
        timer.start()

        print(f"Created {self._age} year old {self._breed} named {self._name}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        self._age = new_age

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, new_breed):
        self._breed = new_breed


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