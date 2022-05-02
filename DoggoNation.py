#! /usr/bin/env python3

from Timer import Timer
from Dog import Dog
import constants
import time
import os

debug = False
trace = True

class DoggoNation():
    def __init__(self):
        print("\nWelcome to Doggo Nation! A place where you can create and interact with virtual dogs.\n")

        self.dog_entries = []


    def enter_doggo(self):
        if debug: print("called enter_doggo()")
        
        self.list_activities("your dog")

        while True:
            # select and process activity
            selected_activity = self.input_activity()
            next_option = self.process_input(selected_activity)
            
            if next_option == constants.EXIT:
                print("\n>>> Goodbye...See you next time!\n")
                break

            if next_option == constants.HELP:
                os.system("clear")
                if len(self.dog_entries) == 0:
                    self.list_activities("your dog")
                    continue

                self.list_activities(self.active_dog.name)

            elif next_option == constants.CREATE:
                os.system("clear")
                print("\n*** Let's Create Your Custom Dog! ***")

                # create custom dog (instantiate Dog class)
                self.create_dog()
                # select dog
                self.active_dog = self.activate_dog()
                continue


            if len(self.dog_entries) == 0:
                print("\n>>> No dogs available...enter 'create' to build a dog")
                continue

            if next_option == constants.NAME:
                print("\n--- Change Dog Name ---")

                new_name = input(f"\nYour dog's current name is {self.active_dog.name}.\n\nEnter your dog's new name: ").lower()

                new_name = new_name[0].upper() + new_name[1:]

                self.active_dog.name = new_name

                print(f"\n>>> Your dog's new name is {self.active_dog.name}.")

            elif next_option == constants.AGE:
                print("\n--- Get Dog Age ---")
                print(f"\n>>> {self.active_dog.name} is {self.active_dog.age} year(s) old.")

            elif next_option == constants.BREED:
                print("\n--- Get Dog Breed ---")
                print(f"\n>>> {self.active_dog.name} is a(n) {self.active_dog.breed}.")

            elif next_option == constants.FEED:
                print(f"\nLet's feed {self.active_dog.name} some kibbles!")
                self.active_dog.eat()

            elif next_option == constants.WALK:
                print(f"\nLet's take {self.active_dog.name} for a walk!")
                self.active_dog.walk()

            elif next_option == constants.POTTY:
                print(f"\nLet's take {self.active_dog.name} to potty!")
                self.active_dog.potty()

            elif next_option == constants.TREAT:
                print(f"\nLet's give {self.active_dog.name} a treat!")
                self.active_dog.treat()

            elif next_option == constants.SLEEP:
                print(f"\nLet's put {self.active_dog.name} down for a nap!")
                self.active_dog.sleep()

            elif next_option == constants.SWITCH:
                if len(self.dog_entries) > 1:
                    self.active_dog = self.activate_dog()

                print("\n>>> Only one dog available...to switch dogs, create a new dog")

            else:
                print(f"\n>>> Unavailable option...enter '{constants.HELP}' for help")


    def create_dog(self):
        if debug: print("called create_dog()")

        while True:
            self.dog_name = input("\nEnter a dog name: ")

            if len(self.dog_name) > 0 and self.dog_name.isalpha():
                break

            print(">>> Enter a valid name")


        while True:
            try:
                self.dog_age = int(input("\nEnter a dog age: "))

                if self.dog_age >= 0:
                    break

                print(">>> Enter a valid age")

            except:
                print(">>> Enter a valid age")


        while True:
            self.dog_breed = input("\nEnter a dog breed: ")

            if len(self.dog_breed) > 0 and self.dog_breed.isalpha():
                break

            print(">>> Enter a valid breed")


        self.entry = Dog(self.dog_name, self.dog_age, self.dog_breed)

        already_exist = False

        for dog in self.dog_entries:
            if dog.name == self.entry.name and dog.age == self.entry.age and dog.breed == self.entry.breed:
                already_exist = True
        
        if not already_exist:
            print(f"\n>>> You created a {self.dog_age} year old {self.dog_breed} named {self.dog_name}!")
            self.dog_entries.append(self.entry)

        else:
            print("\n>>> Dog already exists...create a different dog")
            self.create_dog()


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

            dog_found = False
            index = None

            for dog in dog_list:

                if input_name == dog.name:
                    dog_found = True
                    
                if dog_found:
                    index = dog_list.index(dog)
                    break

            if not dog_found:    
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

        if len(self.dog_entries) > 1:
            print("\n*** Let's Select A Dog! ***")
            self.list_dogs(self.dog_entries)
            activated_dog = self.select_dog(self.dog_entries)

        else:
            activated_dog = self.entry

        return activated_dog
        

    def list_activities(self, dog_name):
        if debug: print("called list_activities()")

        if not dog_name:
            dog_name = "Your Dog"

        self.activities = [f"Change {dog_name}'s name", f"Get {dog_name}'s age", f"Get {dog_name}'s breed", f"Feed {dog_name}", f"Walk {dog_name}", f"Let {dog_name} potty", f"Give {dog_name} a treat", f"Put {dog_name} to bed\n", "Create new dog", "Switch dogs", "Exit program"]

        print(f"\nBelow is a list of activities you can do with {dog_name}:\n")

        for activity in self.activities:
            print(f"- {activity}")


    def input_activity(self):
        if debug: print("called input_activity()")

        # if trace: print(f"Activity List: {activity_list}")

        activity = input(f"\nWhat would you like to do (enter '{constants.HELP}' for help)? ").lower()

        activity = activity.split()

        return activity


    def process_input(self, split_input):
        if debug: print("called process_input()")

        if constants.NAME in split_input: 
            return constants.NAME
            
        if constants.AGE in split_input or constants.OLD in split_input: 
            return constants.AGE

        if constants.BREED in split_input or constants.KIND in split_input: 
            return constants.BREED

        if constants.FEED in split_input or constants.EAT in split_input: 
            return constants.FEED
            
        if constants.WALK in split_input: 
            return constants.WALK
            
        if constants.POTTY in split_input: 
            return constants.POTTY
            
        if constants.TREAT in split_input or constants.SNACK in split_input: 
            return constants.TREAT
            
        if constants.SLEEP in split_input or constants.NAP in split_input or constants.BED in split_input or constants.REST in split_input: 
            return constants.SLEEP

        if constants.EXIT in split_input: 
            return constants.EXIT
            
        if constants.SWITCH in split_input or constants.CHANGE in split_input or constants.INTERACT in split_input or constants.DIFFERENT in split_input or constants.ANOTHER in split_input: 
            return constants.SWITCH

        if constants.CREATE in split_input or constants.NEW in split_input or constants.BUILD in split_input or constants.MAKE in split_input or constants.ADD in split_input: 
            return constants.CREATE
        
        if constants.HELP in split_input:
            return constants.HELP

        return


def main():
    doggo = DoggoNation()

    doggo.enter_doggo()


if __name__ == "__main__":
    main()

