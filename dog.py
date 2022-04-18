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
            print("munch munch munch")
            
            time.sleep(1)
            print(f"{self.name} is done eating")
            
            self.eat_timer.stop()
            self.eat_timer.start()

        else:
            print(f"{self.name} is not hungry")

    
    def walk(self):
        if debug: print("called walk()")

        if self.walk_timer.elapsed_time() >= 12:
            self.is_bored = True
            print("trot trot trot")
            
            time.sleep(1)
            print(f"{self.name} is done walking")
            
            self.walk_timer.stop()
            self.walk_timer.start()

        else:
            print(f"{self.name} does not need a walk")


    def sleep(self):
        if debug: print("called sleep()")

        if self.sleep_timer.elapsed_time() >= 36:
            self.is_tired = True
            print("zzz zzz zzz")

            time.sleep(1)
            print(f"{self.name} is done sleeping")
            
            self.sleep_timer.stop()
            self.sleep_timer.start()

        else:
            print(f"{self.name} is not tired")


def create_dog():
    if debug: print("called create_dog()")

    print("\nLet's Create a Dog!")

    dog_entries = []

    while True:
        dog_name = str(input("\nEnter a dog name (Lima): ")) or "Lima"
        dog_age = input("Enter a dog age (2): ") or 2
        dog_breed = str(input("Enter a dog breed (Malamute): ")) or "Malamute"

        entry = [dog_name, dog_age, dog_breed]

        if entry in dog_entries:
            print("\n>>> ERROR: Dog already exists...create a different dog")
            continue
        
        dog_entries.append(entry)
        new_dog = Dog(dog_name, dog_age, dog_breed)
        
        create_another_dog = input("\nCreate another dog? ").lower()

        if create_another_dog != "y":
            break

    print("\nLet's Interact with a Dog!")
    
    if len(dog_entries) > 1:
        active_dog = select_dog(dog_entries)

    else:
        active_dog = entry
        
    questions = input(f"\nWhat would you like to know about {active_dog[0]}?\n")
    
    # if not action in actions: 
    #     print("That information is unknown")


def select_dog(dog_list):
    if debug: print("called interact_with_dog()")

    print("\nDog List:")
    list_dogs(dog_list)

    while True:
        try:
            selected_dog = int(input("\nEnter the dog number you wish to interact with: "))
    
        except:
            print(">>> ERROR: Enter a valid number")
            continue

        break

    dog_name = dog_list[selected_dog-1][0]  
    dog_age = dog_list[selected_dog-1][1] 
    dog_breed = dog_list[selected_dog-1][2] 
    
    print(f"\n>>> You selected {dog_name} the {dog_age} year old {dog_breed}!")
    
    return dog_list[selected_dog-1]
            

def list_dogs(dog_list):
    if debug: print("called list_dogs()")

    for i, dog in enumerate(dog_list):
        dog_name = dog[0]
        dog_age = dog[1]
        dog_breed = dog[2]
        
        print(f"({i+1}) {dog_name}: {dog_age} year old {dog_breed}")

              
if __name__ == "__main__":
    create_dog()

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

        