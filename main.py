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
        return "\nPlaying tonight is {} {} from {}. The contestant is a {} year old {} who is a {}. \n".format(self.name, self.surname, self.player_location, self.age, self.gender, self.occupation)



# Class for Game
class Game:
   
    round_number = 0 # Used to check on what round the game is 
    QA_pair = {}
    correct_answer = []
    QA_pair_ls = []
    selectors = ['a','b','c','d']
    prize_list = [500, 1000, 2000, 5000, 10000, 20000, 50000, 75000, 150000, 250000, 500000, 1000000]
    game_active = True

    def setQuestions(self):
        with open("Q_n_A.txt") as file:
            
            for record in file:
                temp_ls = record.split('#')
                question = temp_ls[0]
                options = temp_ls[1].split(":")
                self.correct_answer.append(temp_ls[2])
                self.QA_pair[question] = options
        
        self.QA_pair_ls = list(self.QA_pair.items())


    def __repr__(self):
        return self.game_active
    
    def getGameState(self):
        return self.game_active
    
    def question(self):
        index = len(self.QA_pair_ls) - 1; 
        Q_index = random.randint(0,index)
        pair = self.QA_pair_ls[Q_index]
        print(pair[0])
        temp = 0
        for element in pair[1]:
            print(self.selectors[temp] + ". " + str(element) )
            temp += 1
        answer = self.answer()
        if(self.selectors.index(answer) == int(self.correct_answer[Q_index])):
            self.QA_pair_ls.pop(Q_index)
            self.correct_answer.pop(Q_index)
            return True
        else:
            return False


    def answer(self):
        entered_selector = False

        while entered_selector != True:
            answer = input("Select the correct option (eg. a): ")
            lower_answer = answer.lower()
            if( lower_answer == 'a') or ( lower_answer == 'b') or ( lower_answer == 'c') or ( lower_answer == 'd'):
                entered_selector = True

        return lower_answer
    
    def game_logic(self, answer):
        if answer:
            print("\n You have won $" + str(self.prize_list[self.round_number]) + " !!\n")
            self.round_number += 1

            if self.round_number == 15:
                print("You won the game , hope you enjoyed <3")
        else:
            print("Game Over you Lost")
            self.game_active = False

   
            
    
     


# --------------- Variable and Function Declaration ----------------------- 
    
    

# --------------- Main Program ----------------------- 

# Welcome Message
print(" \n Welcome to Who wants to be a Millionare - Computer Science Edition \n\n Please enter your detials below: \n\n")

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
#print(game.question())
while game.getGameState():
   temp = game.question()
   game.game_logic(temp)
   if(game.round_number == 15):
       break
   

## To Do:
# - Take Prize
# - Addition of Comments and Code Explination

