#! /usr/bin/env python3

from timer import Timer
from dog import Dog
import time


debug = False
trace = True

class Doggo_Nation():
    def __init__(self):
        print("\nWelcome to Doggo Nation! A place where you can create and interact with virtual dogs. Let's start by creating your custom dog!")


    def start_doggo(self):
        if debug: print("called start_doggo()")
        
        self.dog_entries = []

        # create custom dog (instantiate Dog class)
        while True:
            self.dog_name = str(input("\nEnter a dog name (Lima): ")) or "Lima"
            self.dog_age = input("Enter a dog age (2): ") or 2
            self.dog_breed = str(input("Enter a dog breed (Malamute): ")) or "Malamute"

            self.entry = [self.dog_name, self.dog_age, self.dog_breed]

            if self.entry in self.dog_entries:
                print("\n>>> ERROR: Dog already exists...create a different dog")
                continue
            
            self.dog_entries.append(self.entry)
            self.new_dog = Dog(self.dog_name, self.dog_age, self.dog_breed)
            
            self.create_another_dog = input("\nCreate another dog? ").lower()

            if self.create_another_dog != "y":
                break

        print("\nLet's Interact with Your Dog!")
        
        # select dog to interact with
        if len(self.dog_entries) > 1:
            self.active_dog = self.select_dog(self.dog_entries)

        else:
            self.active_dog = self.entry

        self.active_dog_name = self.active_dog[0]
        self.list_activities(self.active_dog_name)

        # select dog activity
        self.selected_activity = self.select_activity()

        # process dog activity selections 
        self.process_activity(self.selected_activity)

        

    def list_dogs(self, dog_list):
        if debug: print("called list_dogs()")

        for i, dog in enumerate(dog_list):
            dog_name = dog[0]
            dog_age = dog[1]
            dog_breed = dog[2]
            
            print(f"({i+1}) {dog_name}: {dog_age} year old {dog_breed}")


    def select_dog(self, dog_list):
        if debug: print("called select_dog()")

        print("\nDog List:")
        self.list_dogs(dog_list)

        while True:
            try:
                self.selected_dog = int(input("\nEnter the dog number you wish to interact with: "))
        
            except:
                print(">>> ERROR: Enter a valid number")
                continue

            break

        dog_name = dog_list[self.selected_dog-1][0]  
        dog_age = dog_list[self.selected_dog-1][1] 
        dog_breed = dog_list[self.selected_dog-1][2] 
        
        print(f"\n>>> You selected {dog_name} the {dog_age} year old {dog_breed}!")
        
        return dog_list[self.selected_dog-1]
                

    def list_activities(self, dog_name):
        if debug: print("called list_activities()")

        self.actions = ["get dog's name", f"change {dog_name}'s name", f"get {dog_name}'s age", f"get {dog_name}'s breed", f"feed {dog_name}", f"walk {dog_name}", f"put {dog_name} to bed"]

        print(f"\nBelow is a list of activities you can do with {dog_name}:\n")

        for i, action in enumerate(self.actions):
            print(f"({i+1}) {action}")


    def select_activity(self):
        if debug: print("called select_activity()")

        while True:
            try:
                self.activity_number = int(input(f"\nEnter an activity number: "))

            except:
                print(">>> ERROR: Enter a valid number")
                continue

            if self.activity_number > len(self.actions) or self.activity_number <= 0:
                print(">>> ERROR: That number is not listed")
                continue
            
            break

        return self.activity_number-1


    def process_activity(self, activity_number):
        if debug: print("called process_activity()")

        # if trace: print(f"Activity Number is {activity_number}")

        if activity_number == 0: 
            print(f"\n>>> Your dog's name is {self.new_dog.name}")


def enter_doggo():
    doggo = Doggo_Nation()

    doggo.start_doggo()


if __name__ == "__main__":
    enter_doggo()
