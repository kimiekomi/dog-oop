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

        while True:
            self.list_activities(self.active_dog_name)

            # select dog activity
            self.selected_activity = self.select_activity()

            # process dog activity selections 
            self.process_activity(self.selected_activity)

            will_continue = input(f"\nWould you like to keep interacting with {self.active_dog_name} (y/n)? ").lower()

            if will_continue != "y":
                os.system("clear")

                self.list_options()

                while True:
                    try:
                        option_number = int(input("\nEnter desired option number: "))-1

                    except:
                        print(">>> ERROR: Enter a valid number")
                        continue
                    
                    if option_number > len(self.options) or self.activity_number <= 0:
                        print(">>> ERROR: That number is not listed")
                        continue 

                    break

                if option_number == 0:
                    print("\nFeature not implemented yet\n")
                    break

                if option_number == 1:
                    print("\nFeature not implemented yet\n")
                    break

                if option_number == 2:
                    print("\nGoodbye...See you next time!\n")
                    break

            os.system("clear")

        # remove will_continue
        # change menu input...don't accept numbers...split input use contain()
        # add feature to switch dogs or create new dog(s)
        # might need separate create_dog() and interact_dog() 
        # add option to potty, treat
        # remove timer from walk


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

        self.actions = ["get dog's name", f"change {dog_name}'s name", f"get {dog_name}'s age", f"get {dog_name}'s breed", f"feed {dog_name}", f"walk {dog_name}", f"let {dog_name} potty", f"put {dog_name} to bed"]

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
            print(f"\n>>> Your dog's name is {self.new_dog.name}.")

        if activity_number == 1: 
            new_name = input(f"\nYour dog's current name is {self.new_dog.name}.\nEnter your dog's new name: ")

            new_name = new_name[0].upper() + new_name[1:]

            self.new_dog.name = new_name
            self.active_dog_name = new_name

            print(f"\n>>> Your dog's name is now {self.new_dog.name}.")

        if activity_number == 2: 
            print(f"\n>>> Your dog is {self.new_dog.age} year(s) old.")

        if activity_number == 3: 
            print(f"\n>>> Your dog is a(n) {self.new_dog.breed}.")

        if activity_number == 4: 
            print(f"\nLet's feed {self.new_dog.name} some kibbles!")
            self.new_dog.eat()

        if activity_number == 5:
            print(f"\nLet's take {self.new_dog.name} for a walk!")
            self.new_dog.walk()

        if activity_number == 6:
            print(f"\nLet's take {self.new_dog.name} to potty!")
            self.new_dog.potty()

        if activity_number == 7:
            print(f"\nLet's put {self.new_dog.name} down for a nap!")
            self.new_dog.sleep()


    def list_options(self):
        if debug: print("called list_options()")

        self.options = ["Create a new dog", "Switch to a different dog", "Exit Program"]

        print("\nWhat would you like to do next?")

        for i, self.option in enumerate(self.options):
            print(f"({i+1}) {self.option}")

    
    def select_option(self):
        pass


    def process_option(self):
        pass


def enter_doggo():
    doggo = Doggo_Nation()

    doggo.start_doggo()


if __name__ == "__main__":
    enter_doggo()

