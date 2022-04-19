#! /usr/bin/env python3

from timer import Timer
from dog import Dog
import time
import os

debug = False
trace = True

class Doggo_Nation():
    def __init__(self):
        print("\nWelcome to Doggo Nation! A place where you can create and interact with virtual dogs.\n")


    def start_doggo(self):
        if debug: print("called start_doggo()")
        
        self.dog_entries = []

        # create custom dog (instantiate Dog class)
        while True:
            print("\n*** Let's Create Your Custom Dog! ***")

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

        os.system("clear")

        print("\n*** Let's Interact with Your Dog! ***")
        
        # select dog to interact with
        if len(self.dog_entries) > 1:
            self.active_dog = self.select_dog(self.dog_entries)

        else:
            self.active_dog = self.entry
        
        self.active_dog_name = self.active_dog[0]

        self.list_activities(self.active_dog_name)

        while True:

            # select dog activity
            self.selected_activity = self.select_activity(self.activities)

            # process dog activity selections 
            next_option = self.process_activity(self.selected_activity)

            # if trace: print(f"Next Option: {next_option}")

            if next_option == 0:
                break

            # os.system("clear")


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

        self.activities = [f"Change {dog_name}'s name", f"Get {dog_name}'s age", f"Get {dog_name}'s breed", f"Feed {dog_name}", f"Walk {dog_name}", f"Let {dog_name} potty", f"Give {dog_name} a treat", f"Put {dog_name} to bed\n", "Create new dog", "Switch dogs", "Exit program"]

        print(f"\nBelow is a list of activities you can do with {dog_name}:\n")

        for activity in self.activities:
            print(f"- {activity}")


    def select_activity(self, activity_list):
        if debug: print("called select_activity()")

        # if trace: print(f"Activity List: {activity_list}")

        activity = input(f"\nWhat would you like to do? ").lower()

        activity = activity.split()

        return activity


    def process_activity(self, split_activity):
        if debug: print("called process_activity()")

        if "name" in split_activity: 
            new_name = input(f"\nYour dog's current name is {self.new_dog.name}.\nEnter your dog's new name: ")

            new_name = new_name[0].upper() + new_name[1:]

            self.new_dog.name = new_name
            self.active_dog_name = new_name

            print(f"\n>>> Your dog's name is now {self.new_dog.name}.")

        elif "age" in split_activity: 
            print(f"\n>>> Your dog is {self.new_dog.age} year(s) old.")

        elif "breed" in split_activity: 
            print(f"\n>>> Your dog is a(n) {self.new_dog.breed}.")

        elif "feed" in split_activity: 
            print(f"\nLet's feed {self.new_dog.name} some kibbles!")
            self.new_dog.eat()

        elif "walk" in split_activity: 
            print(f"\nLet's take {self.new_dog.name} for a walk!")
            self.new_dog.walk()

        elif "potty" in split_activity: 
            print(f"\nLet's take {self.new_dog.name} to potty!")
            self.new_dog.potty()

        elif "treat" in split_activity: 
            print(f"\nLet's give {self.new_dog.name} a treat!")
            self.new_dog.treat()

        elif "sleep" in split_activity: 
            print(f"\nLet's put {self.new_dog.name} down for a nap!")
            self.new_dog.sleep()

        elif "new" in split_activity: 
            print(f"\nFeature not implemented yet...")
        
        elif "switch" in split_activity: 
            print(f"\nFeature not implemented yet...")

        elif "exit" in split_activity: 
            print("\nGoodbye...See you next time!\n")
            return 0

        else: 
            print(">>> ERROR: That option is not available")


    def select_option(self):
        pass


    def process_option(self):
        pass


def enter_doggo():
    doggo = Doggo_Nation()

    doggo.start_doggo()


if __name__ == "__main__":
    enter_doggo()

