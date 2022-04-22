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
        
        # create custom dog (instantiate Dog class)
        self.create_dog()
        
        os.system("clear")

        self.active_dog = self.activate_dog()

        while True:
            # if trace: print(f"Active Dog: {self.active_dog}")

            print("\n*** Let's Interact with Your Dog! ***")
            
            # select dog activity
            selected_activity = self.input_activity()
            # process dog activity selections 
            next_option = self.process_input(selected_activity)

            if next_option == "exit":
                print("\nGoodbye...See you next time!\n")
                break

            if next_option == "name":
                new_name = input(f"\nYour dog's current name is {self.active_dog.name}.\nEnter your dog's new name: ")

                new_name = new_name[0].upper() + new_name[1:]

                self.active_dog.name = new_name

                print(f"\n>>> Your dog's name is now {self.active_dog.name}.")

            elif next_option == "age":
                print(f"\n>>> Your dog is {self.active_dog.age} year(s) old.")

            elif next_option == "breed":
                print(f"\n>>> Your dog is a(n) {self.active_dog.breed}.")

            elif next_option == "feed":
                print(f"\nLet's feed {self.active_dog.name} some kibbles!")
                self.active_dog.eat()

            elif next_option == "walk":
                print(f"\nLet's take {self.active_dog.name} for a walk!")
                self.active_dog.walk()

            elif next_option == "potty":
                print(f"\nLet's take {self.active_dog.name} to potty!")
                self.active_dog.potty()

            elif next_option == "treat":
                print(f"\nLet's give {self.active_dog.name} a treat!")
                self.active_dog.treat()

            elif next_option == "sleep":
                print(f"\nLet's put {self.active_dog.name} down for a nap!")
                self.active_dog.sleep()

            elif next_option == "switch":
                if len(self.dog_entries) > 1:
                    self.active_dog = self.activate_dog()

                print("There is only one dog available...")

            elif next_option == "new":
                self.create_dog()
                self.active_dog = self.activate_dog()

            elif next_option == "m":
                self.list_activities(self.active_dog.name)

            else:
                print(">>> ERROR: unavailable option")


    def create_dog(self):
        if debug: print("called create_dog()")

        self.dog_entries = []

        while True:
            print("\n*** Let's Create Your Custom Dog! ***")

            self.dog_name = str(input("\nEnter a dog name (Lima): ")) or "Lima"
            self.dog_age = input("Enter a dog age (2): ") or 2
            self.dog_breed = str(input("Enter a dog breed (Malamute): ")) or "Malamute"

            self.dog_name = self.dog_name[0].upper() + self.dog_name[1:].lower()
            self.dog_breed = self.dog_breed[0].upper() + self.dog_breed[1:].lower()

            self.entry = Dog(self.dog_name, self.dog_age, self.dog_breed)

            if self.entry in self.dog_entries:
                print("\n>>> ERROR: Dog already exists...create a different dog")
                continue
            
            self.dog_entries.append(self.entry)
            
            self.create_another_dog = input("\nCreate another dog? ").lower()

            if self.create_another_dog != "y":
                break


    def list_dogs(self, dog_list):
        if debug: print("called list_dogs()")

        print("\nDog List:")

        for dog in dog_list:
            dog_name = dog.name
            dog_age = dog.age
            dog_breed = dog.breed
            
            print(f"{dog_name}: {dog_age} year old {dog_breed}")


    def select_dog(self, dog_list):
        if debug: print("called select_dog()")

        # if trace: print(f"Dog List: {dog_list}")

        while True:
            input_name = input("\nEnter the dog's name you wish to interact with: ")

            input_name = input_name[0].upper() + input_name[1:].lower()

            count = 0
            index = None

            for dog in dog_list:

                if input_name == dog.name:
                    count += 1
                    index = dog_list.index(dog)

            if count == 0:    
                print("Dog not found")
                continue
            
            break

        selected_dog = dog_list[index]

        dog_name = selected_dog.name
        dog_age = selected_dog.age
        dog_breed = selected_dog.breed

        print(f"\n>>> You selected {dog_name} the {dog_age} year old {dog_breed}!")
        return selected_dog


    def activate_dog(self):
        if debug: print("called activate_dog()")

        print("\n*** Let's Select A Dog! ***")

        if len(self.dog_entries) > 1:
            self.list_dogs(self.dog_entries)
            activated_dog = self.select_dog(self.dog_entries)

        else:
            activated_dog = self.entry

        return activated_dog
        

    def list_activities(self, dog_name):
        if debug: print("called list_activities()")

        self.activities = [f"Change {dog_name}'s name", f"Get {dog_name}'s age", f"Get {dog_name}'s breed", f"Feed {dog_name}", f"Walk {dog_name}", f"Let {dog_name} potty", f"Give {dog_name} a treat", f"Put {dog_name} to bed\n", "Create new dog", "Switch dogs", "Exit program"]

        print(f"\nBelow is a list of activities you can do with {dog_name}:\n")

        for activity in self.activities:
            print(f"- {activity}")


    def input_activity(self):
        if debug: print("called input_activity()")

        # if trace: print(f"Activity List: {activity_list}")

        activity = input(f"\nWhat would you like to do (enter 'm' to view full menu)? ").lower()

        activity = activity.split()

        return activity


    def process_input(self, split_input):
        if debug: print("called process_input()")


        if "name" in split_input: 
            return "name"
            
        elif "age" in split_input: 
            return "age"

        elif "breed" in split_input: 
            return "breed"

        elif "feed" in split_input: 
            return "feed"
            
        elif "walk" in split_input: 
            return "walk"
            
        elif "potty" in split_input: 
            return "potty"
            
        elif "treat" in split_input: 
            return "treat"
            
        elif "sleep" in split_input: 
            return "sleep"

        elif "exit" in split_input: 
            return "exit"
            
        elif "switch" in split_input: 
            return "switch"

        elif "new" in split_input: 
            return "new"
        
        elif "m" in split_input:
            return "m"

        else: 
            return


def enter_doggo():
    doggo = Doggo_Nation()

    doggo.start_doggo()


if __name__ == "__main__":
    enter_doggo()

