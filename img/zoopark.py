import random
import colorama
import os
import time
import string

from colorama import Fore, Back, Style, init
from abc import ABC, abstractmethod
from array import array

from enum import Enum
from dataclasses import dataclass

def clear_terminal(): # Clearing the terminal:
    import platform
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

class PetOwner:
    def __init__(self, name):
        self.__name = name  # Note the access directive private
        self.__animals = []

    def print_animals(self):
        try:
            clear_terminal()  # Clearing the terminal
        except Exception as e:
            print(f"Error clearing the terminal: {str(e)}")
        
        if not self.__animals:
            print(Fore.RED + "No animals exist yet" + Fore.RESET)
        else:
            print(Fore.CYAN + "ANIMALS:")
            print("------------------------" + Fore.RESET)
            print(Fore.RESET)
                
        for i, animal in enumerate(self.__animals):
            if isinstance(animal, Dog):
                favourite_food = animal.favourite_food  # Access the favourite food attribute of the Dog instance
            elif isinstance(animal, Cat):
                favourite_food = animal.favourite_food
            
            print(f"Animal {i+1} ({type(animal).__name__})")
            print(f"Name: {animal.name}")
            print(f"Age: {animal.age} years old")
            if isinstance(animal, Dog):
                print(f"Favourite Food: {favourite_food}")
            elif isinstance(animal, Cat):
                print(f"No favourite food recorded.")
            print()  # Empty line for better readability
            print("------------------------")
                
    def play(self):
        if not self.__animals:
            clear_terminal() # Clearing the terminal
            print(Fore.RED + "There are no animals to play with right now." + Fore.RESET)
            return
        
        for animal in self.__animals:
            clear_terminal() # Clearing the terminal
            print(f"What do you want to do with {animal.name}? Play / Social / Sleep")
            action = input(f"What do you want to do with {animal.name}?")
            
            if action.lower() == 'play':
                if isinstance(animal, Dog):
                    print(f"The dog jumps up and down and excited!")
                elif isinstance(animal, Cat):
                    print(f"The cat is purring and rubbing against you.")
            elif action.lower() == 'Social':
                print(f"You're now petting {animal.name}.")
            elif action.lower() == 'sleep':
                print(f"{animal.name} is now hitting the hay. zzZZZZZZ")

    def ViewStats(self):
        for animal in self.__animals:
            if isinstance(animal, Dog) or isinstance(animal, Cat):
                print(Fore.YELLOW + "Animal Stats" + Fore.RESET)
                print("----------------------")

                # Calculate the hunger level based on the hunger rate and time elapsed
                hunger_level = animal.hunger_rate * (time.time() - animal._last_feeding_time)

                # Display hunger level with a maximum of 10
                print(f"{animal.get_name()} (Type: {type(animal).__name__}): Hunger Level {min(hunger_level, 10)} / 10")
                
    def update_last_feeding_time(self, animal):
        animal._last_feeding_time = time.time()
            
    @abstractmethod
    def Feed(self, animal):
        if isinstance(animal, Dog) or isinstance(animal, Cat):
            # Increase hunger level by 4
            animal.hunger_level = max(0, animal.hunger_level + 4)

            # Update last feeding time
            self.update_last_feeding_time(animal)
            
    def Run(self):
        clear_terminal() # Clearing the terminal 
        print(Style.BRIGHT)
        print(Fore.YELLOW + "ANIMAL ZOOPARK SIMULATOR" + Fore.RESET)
        print(Fore.YELLOW + "--------------------------")
        print(Fore.RESET)
        self.__name = input("Please enter your name: ")
        clear_terminal()
        while True:
            print(Fore.GREEN)
            print("""
 .+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+. 
(      _____           ____            _          )
 )    |__  /___   ___ |  _ \ __ _ _ __| | __     ( 
(       / // _ \ / _ \| |_) / _` | '__| |/ /      )
 )     / /| (_) | (_) |  __/ (_| | |  |   <      ( 
(     /____\___/ \___/|_|   \__,_|_|  |_|\_\      )
 )                                               ( 
(                                                 )
 "+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+" 
""")
            print("\nMade by Buffal0x")
            print("\nhttps://buffal0x.github.io")
            print(Fore.RESET)
            print("\nPython - Animal Zoo Menu:")
            print("-------------------------------------")
            print(f"Hello, {self.__name}!")
            print(f"Connected to da best zoo network")
            print("-------------------------------------")
            print(Fore.GREEN + "1. View Animals" + Fore.RESET)
            print(Fore.YELLOW + "2. Feed an Animal" + Fore.RESET)
            print(Fore.BLUE + "3. Play with an Animal" + Fore.RESET)
            print(Fore.CYAN + "4. Add a New Animal" + Fore.RESET)
            print(Fore.MAGENTA + "5. Remove an Existing Animal" + Fore.RESET)
            print(Fore.MAGENTA + "6. View the animals stats" + Fore.RESET)
            print(Fore.YELLOW + "7. Auto-generate animals" + Fore.RESET)
            print(Fore.RED + "8. Quit" + Fore.RESET)
            print("--------------------------")
            choice = input("Choose an option: ")

            if choice == '1':
                clear_terminal() # Clearing the terminal # Clearing the terminal
                self.print_animals()
            elif choice == '2':
                if len(self.__animals) == 0:
                    clear_terminal() # Clearing the terminal # Clearing the terminal
                    print(Fore.RED + "No animals available to feed." + Fore.RESET)
                else:
                    clear_terminal() # Clearing the terminal # Clearing the terminal
                    print("\nAvailable Animals:")
                    print("--------------------------")
                    for i, animal in enumerate(self.__animals):
                        print(f"{i + 1}. {animal.get_name()} ({type(animal).__name__})")
                    food_choice = input("Enter the number of the animal you want to feed, and then type the food (e.g. carrots): ")
                    
                    if food_choice.isdigit() and 1 <= int(food_choice) <= len(self.__animals):
                        food = input(f"Enter {self.__animals[int(food_choice) - 1].get_name()}'s food: ")
                        
                        self.__animals[int(food_choice) - 1].eat(food)
            elif choice == '3':
                clear_terminal() # Clearing the terminal # Clearing the terminal
                self.play()
            elif choice == '4':
                clear_terminal() # Clearing the terminal # Clearing the terminal
                animal_type = input("What type of animal do you want to add? (Dog, Cat, Wolf, Lion or Lioncub): ").lower()
                age = int(input("How old is the animal? "))
                name = input("What's the animal's name? ")
                
                if animal_type == "dog":
                    self.__animals.append(Dog(age, name))
                    clear_terminal() # Clearing the terminal # Clearing the terminal
                    print(Fore.GREEN + f"You added a dog named '{name}' who is '{age}' yrs" + Fore.RESET)
                elif animal_type == "cat":
                    self.__animals.append(Cat(age, name))
                    clear_terminal() # Clearing the terminal # Clearing the terminal
                    print(Fore.GREEN + f"You added a cat named '{name}' who is '{age}' yrs" + Fore.RESET)
                elif animal_type == "wolf":
                    self.__animals.append(Wolf(age, name))
                    clear_terminal() # Clearing the terminal # Clearing the terminal
                    print(Fore.GREEN + f"You added a cat named '{name}' who is '{age}' yrs" + Fore.RESET)
                elif animal_type == "lion":
                    self.__animals.append(Lion(age, name))
                    clear_terminal() # Clearing the terminal # Clearing the terminal
                    print(Fore.GREEN + f"You added a cat named '{name}' who is '{age}' yrs" + Fore.RESET)
                elif animal_type == "lioncub":
                    self.__animals.append(LionCub(age, name))
                    clear_terminal() # Clearing the terminal # Clearing the terminal
                    print(Fore.GREEN + f"You added a cat named '{name}' who is '{age}' yrs" + Fore.RESET)
                else:
                    print(Fore.RED + "Invalid animal type!" + Fore.RESET)
            elif choice == '5':
                clear_terminal() # Clearing the terminal # Clearing the terminal
                if len(self.__animals) == 0:
                    print(Fore.RED + "No animals available to remove." + Fore.RESET)
                else:
                    print("\nAvailable Animals:")
                    print("--------------------------")
                    for i, animal in enumerate(self.__animals):
                        print(f"{i + 1}. {animal.get_name()} ({type(animal).__name__})")
                    removal_choice = input("Enter the number of the animal you want to remove, and then type 'remove': ")
                    
                    if removal_choice.isdigit() and 1 <= int(removal_choice) <= len(self.__animals):
                        self.__animals[int(removal_choice) - 1].interact()
                        print(Fore.RED + f"\n{self.__animals[int(removal_choice) - 1].get_name()} has been removed from your collection." + Fore.RESET)
                        self.__animals.pop(int(removal_choice) - 1)
                    else:
                        print(Fore.RED + "Invalid option!" + Fore.RESET)
            elif choice == '6':
                clear_terminal()
                self.ViewStats()
            elif choice == '7':
                animal_types = ["cat", "dog","wolf","lion","lioncub"]  # Creating a list of animal types
                names = ["Bella", "Buddy", "Max", "Molly", "Oliver", "Riley", "Sadie"]  # Creating a list of names
                favourite_foods = ["Chicken", "Fish", "Steak", "Vegetables", "Pizza","Grass", "Meat", "Cow"]   # Creating a list of foods
            
                animal_type = random.choice(animal_types)  # Randomly selecting an animal type
                age = random.randint(1, 19)  # Randomly generating an age between 1 and 20
                months = random.randint(1,9)
                name = random.choice(names)  # Randomly selecting a name from the list of names
                favourite_food = random.choice(favourite_foods)   # Randomly selecting a food from the list of foods

                if len(self.__animals) < 0:
                    print("ERROR")
                else:
                    if animal_type == "cat":
                        self.__animals.append(Cat(age, name, favourite_food))
                    elif animal_type == "dog":
                        self.__animals.append(Dog(age, name, favourite_food))
                    elif animal_type == "wolf":
                        self.__animals.append(Wolf(age, name, favourite_food))
                    elif animal_type == "lion":
                        self.__animals.append(Lion(age, name, favourite_food))
                    elif animal_type == "lioncub":
                        self.__animals.append(LionCub(months, name, favourite_food))

                    clear_terminal()   # Clearing the terminal
                    print(Fore.GREEN  + f"You added a '{animal_type}' named '{name}' who is {age} yrs old and likes to eat {favourite_food}"  + Fore.RESET)
            elif choice == '8':
                clear_terminal()
                break
            else:
                print(Fore.RED + "Invalid option!" + Fore.RESET)

class Animal(ABC):
    def __init__(self, age, name):
        self._age = age
        self._name = name
        self._last_feeding_time = None  # Initialize last feeding time
        self.hunger_rate = 0.5 # 50% Speed of hunger rate
        self.hunger_level = random.randint(1, 10)  # Generate random hunger level between 1 and 10

    @abstractmethod  # For the class to become abstract
    def eat(self, food):
        if (food == self._favourite_food):
            print("The animal is full!")
        else:
            print("The animal is hungry!")

    def get_name(self):
        return self._name

    def interact(self):
        print("The animal is very pleased!")

    def __str__(self):
        return f"Animal:\n{self._age} years old \nNamed: {self._name}"
    

class Dog(Animal):
    def __init__(self, age, name, feeding_rate=1):  # Added 'feeding_rate' attribute
        super().__init__(age, name)
        self.age = age  # Define the age attribute
        self.name = name
        self._last_feeding_time = 0
        self.favourite_food = "Beef"  # Example favourite food for Dog
    
    def eat(self, food):
        clear_terminal() # Clearing the terminal # Clearing the terminal
        print(f"You gave the dog {food}!")

    def interact(self):
        clear_terminal() # Clearing the terminal # Clearing the terminal
        print("The dog is wagging its tail.")
        
    def ViewStats(self):
        print(f"Name: {self.get_name()}")
        print(f"Age: {self._age}")
        print(f"Hunger level: {self.hunger_level * 100}%")

class Cat(Animal):
    def __init__(self, age, name,feeding_rate=1):
        super().__init__(age, name)
        self.age = age  # Define the age attribute
        self.name = name
        self._last_feeding_time = 0
        self.favourite_food = "Tuna"  # Example favourite food for Dog
        
    def eat(self, food):
        clear_terminal() # Clearing the terminal
        print(f"You gave the cat {food}!")

    def interact(self):
        clear_terminal() # Clearing the terminal
        print("The cat is purring.")
        
    def ViewStats(self):
        print(f"Name: {self.get_name()}")
        print(f"Age: {self._age}")
        print(f"Hunger level: {self.hunger_level * 100}%")

class Wolf(Animal):
    def __init__(self, age, name,feeding_rate=1):
        super().__init__(age, name)
        self.age = age  # Define the age attribute
        self.name = name
        self._last_feeding_time = 0
        self.favourite_food = "Tuna"  # Example favourite food for Dog
        
    def eat(self, food):
        clear_terminal() # Clearing the terminal
        print(f"You gave the wolf {food}!")

    def interact(self):
        clear_terminal() # Clearing the terminal
        print("The wolf is hauling!")
        
    def ViewStats(self):
        print(f"Name: {self.get_name()}")
        print(f"Age: {self._age}")
        print(f"Hunger level: {self.hunger_level * 100}%")

class Lion(Animal):
    def __init__(self, age, name,feeding_rate=1):
        super().__init__(age, name)
        self.age = age  # Define the age attribute
        self.name = name
        self._last_feeding_time = 0
        self.favourite_food = "Tuna"  # Example favourite food for Dog
        
    def eat(self, food):
        clear_terminal() # Clearing the terminal
        print(f"You gave the lion {food}!")

    def interact(self):
        clear_terminal() # Clearing the terminal
        print("The lion is purring.")
        
    def ViewStats(self):
        print(f"Name: {self.get_name()}")
        print(f"Age: {self._age}")
        print(f"Hunger level: {self.hunger_level * 100}%")

class LionCub(Lion, Animal):
    def __init__(self, months, name,feeding_rate=1):
        super().__init__(months / 12, name)
        self._months = months  # Define the age attribute
        self.name = name
        self._last_feeding_time = 0
        self.favourite_food = "Tuna"  # Example favourite food for Dog
        
    def eat(self, food):
        clear_terminal() # Clearing the terminal
        print(f"You gave the lioncub {food}!")

    def interact(self):
        clear_terminal() # Clearing the terminal
        print("The lioncub is running around.")
        
    def ViewStats(self):
        print(f"Name: {self.get_name()}")
        print(f"Age: {self._age}")
        print(f"Hunger level: {self.hunger_level * 100}%")

Jocke = PetOwner("Jocke")
Jocke.Run()