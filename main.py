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
    # List Declarations
    player_prize_money = []
    still_playing = True # Used to check if the player is still in the game
    
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



# Class for Game
class Game:
   
    round_number = 0 # Used to check on what round the game is 
    QA_pair = {}
    correct_answer = []

    def setQuestions(self):
        with open("Q_n_A.txt") as file:
            
            for record in file:
                temp_ls = record.split('#')
                question = temp_ls[0]
                options = temp_ls[1].split(":")
                self.correct_answer.append(temp_ls[2])
                self.QA_pair[question] = options
            
            

     


# --------------- Variable and Function Declaration ----------------------- 
    
    

# --------------- Main Program ----------------------- 

# Welcome Message
print("Welcome to Who wants to be a Millionare - Computer Science Edition \n\n Please enter your detials below: \n\n")

# Get User Input
name = input("Please enter your name: ")
surname = input("Please enter your surname: ")
occupation = input("Please enter your occupation: ")
location = input("Please enter your location: ")
gender = input("Please enter your gender: ")
age = input("Please enter your age: ")

# Init First object (Player)

player = Player(name,surname,age,occupation,location,gender)
print(player)
game = Game()
game.setQuestions()