#! /usr/bin/env python3

from timer import Timer
import time

debug = False
trace = True

class Dog:
    def __init__(self, name, age, breed):
        self._name = name[0].upper() + name[1:].lower()
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

        print(f"\n>>> You created a {self._age} year old {self._breed} named {self._name}!")

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


    def print(self):
        print(f"{self.name}: {self.age} year old {self.breed}")


    def eat(self):
        if debug: print("called eat()")

        if self.eat_timer.elapsed_time() >= 5:
            self.is_hungry = True
            print("\nmunch munch munch")
            
            time.sleep(1)
            print(f"{self.name} is done eating")
            
            self.eat_timer.stop()
            self.eat_timer.start()

        else:
            print(f"\n{self.name} is not hungry")

    
    def walk(self):
        if debug: print("called walk()")

        if self.walk_timer.elapsed_time() >= 12:
            self.is_bored = True
            print("\ntrot trot trot")
            
            time.sleep(1)
            print(f"{self.name} is done walking")
            
            self.walk_timer.stop()
            self.walk_timer.start()

        else:
            print(f"\n{self.name} does not need a walk")


    def sleep(self):
        if debug: print("called sleep()")

        if self.sleep_timer.elapsed_time() >= 36:
            self.is_tired = True
            print("\nzzz zzz zzz")

            time.sleep(1)
            print(f"{self.name} is done sleeping")
            
            self.sleep_timer.stop()
            self.sleep_timer.start()

        else:
            print(f"\n{self.name} is not tired")


if __name__ == "__main__":
    dog = Dog()

    # dog = Dog("Lima", 2, "Malamute")
    # time.sleep(5)
    # dog.eat()
    # time.sleep(3)
    # dog.eat()
    # time.sleep(3)
    # dog.eat()

    # print(dog.breed)
    # dog.breed = "Corgi"
    # dog.print()

    # select_dog([['Lima', 2, 'Malamute'], ['Ruby', 2, 'Malamute'], ["Zula", 2, "Malamute"]])
    # select_dog([['Lima', 2, 'Malamute'], ['Lima', 5, 'Corgi'], ["Zula", 2, "Malamute"], ["Alpha", 3, "Malamute"]])

