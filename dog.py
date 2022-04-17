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

    
    def check_time(self):
        if debug: print("called check_time()")

        if self.start_time == None:
            print("Timer has NOT started")

        self.current_time = time.perf_counter()

        print(f"Current Time: {self.current_time:0.1f}")

        return self.current_time


    def stop(self):
        if debug: print("called stop()")

        if self.start_time == None:
            print("Timer has NOT started")

        self.stop_time = time.perf_counter()
        self.start_time = None

        if trace: print(f"Stop Time: {self.stop_time:0.1f}")

    
    def elapsed_time(self):
        if debug: print("called elapsed_time()")

        if self.start_time == None:
            print("Timer has NOT started")

        self.elapsed_time = self.stop_time - self.start_time

        if trace: print(f"Elapsed Time: {self.elapsed_time:0.1f} seconds")

        return self.elapsed_time


class Dog:
    def __init__(self, name, age, breed):
        self._name = name
        self._age = age
        self._breed = breed

        self.is_hungry = False
        self.is_bored = False
        self.is_tired = False

        self.eat_timer = Timer()
        self.eat_timer.start()

        self.walk_timer = Timer()
        self.walk_timer.start()

        self.sleep_timer = Timer()
        self.sleep_timer.start()

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

        if self.eat_timer.elapsed_time() >= 18:
            self.is_hungry = True
            print("munch munch munch")
            self.eat_etimer.stop()
            self.eat_timer.start()

        else:
            print(f"{self.name} is not hungry")

    
    def walk(self):
        if debug: print("called walk()")

        if self.walk_timer.elapsed_time() >= 12:
            self.is_bored = True
            print("trot trot trot")
            self.walk_timer.stop()
            self.walk_timer.start()

        else:
            print(f"{self.name} does not need a walk")


    def sleep(self):
        if debug: print("called sleep()")

        if self.sleep_timer.elapsed_time() >= 36:
            self.is_tired = True
            print("zzz zzz zzz")
            self.sleep_timer.stop()
            self.sleep_timer.start()

        else:
            print(f"{self.name} is not tired")


def create_dog():
    dog = Dog("Lima", 2, "Malamute")




if __name__ == "__main__":
    create_dog()