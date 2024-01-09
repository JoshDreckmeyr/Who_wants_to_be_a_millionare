# Josh Dreckmeyr - Codecademy Computer Science Career Path
# Intro To Programming -  Portfolio Project
# Explore "Who Wants to Be a Millionaire - Computer Science Edition" 
# a dynamic Codecademy portfolio project. Dive into a unique twist on the classic game show with questions solely centered 
# around the thrilling realm of computer science. Test your coding knowledge in this engaging experience!


# --------------- imports ----------------------- 
import random
import csv
# --------------- Class Declaration ----------------------- 
# Class for Player
class Player:
    
    # Constructor for the Player Class . Sets basic information.
    def __init__(self, player_name, player_surname, player_age, player_occupation, player_location, player_gender):
        self.name = player_name
        self.surname = player_surname
        self.age = player_age
        self.occupation = player_occupation
        self.player_location = player_location
        self.gender = player_gender
    
    # Description returns a String containing the objects basic information
    def __repr__(self):
        return "Playing tonight is {} {} from {}. The contestant is a {} year old {} who is a {}.".format(self.name, self.surname, self.player_location, self.age, self.gender, self.occupation)

# --------------- Variable and Function Declaration ----------------------- 
    
round_number = 0 # Used to check on what round the game is 
still_playing = True # Used to check if the player is still in the game

# --------------- Main Program ----------------------- 

# Welcome Message
print("Welcome to Who wants to be a Millionare - Computer Science Edition")

# Get User Input
name = input("Please Enter your name: ")
surname = input("Please Enter your surname: ")
occupation = input("Please Enter your occupation: ")
location = input("Please Enter your location: ")
gender = input("Please Enter your gender: ")
age = input("Please Enter your age: ")

# Init First object (Player)

player = Player(name,surname,age,occupation,location,gender)
print(player)
