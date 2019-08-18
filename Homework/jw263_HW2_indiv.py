#James Wang
#I211
#Indiv. HW2
#Team 13

#1
#Write a function that takes a one letter abbreviation for a day of the week and returns the full day.
#You may not use lists or tuples as part of your solution.
#Make sure you can handle invalid inputs.
#print(fullweek("R"))
#>>> 
#Thursday

weekDay_Abrv = {
    "M": "Monday",
    "T": "Tuesday",
    "W": "Wednesday",
    "R": "Thursday",
    "F": "Friday",
    "S": "Saturday",
    "U": "Sunday"
}


def fullweek(AbrvString):
    if AbrvString.upper() in weekDay_Abrv:
        return weekDay_Abrv[AbrvString]
    else:
        return "Abbreviation not found."


print("Possible abbreviations: M, T, W, R, F, S, U")
print(fullweek(str(input("Enter a weekday abbreviation: "))))

#2
#Write a function that keeps the user in a loop,
#asking them to enter a one letter abbreviation for the day of the week or DONE.
#As long as they don’t say done, try and translate the abbreviations. If they say DONE, stop.


def weekAbrvLoop():
    while True:
        letter = str(input("Please enter a one letter abbreviation."))
        if letter == "DONE":
            print("DONE!")
            break
        else:
            print(fullweek(letter))

weekAbrvLoop()

#3
#Write a program to implement a rock paper scissors game.

import random
def RockPaperScissors():
    user_input = input("Choose rock, paper, or scissors")
    computer_options = ["rock", "paper", "scissors"]
    computer_option = random.randint(0,2)

    if computer_options[computer_option] == "rock" and user_input == "scissors":
        print("The computer won with rock.")
    elif computer_options[computer_option] == "paper" and user_input == "rock":
        print("The computer won with paper.")
    elif computer_options[computer_option] == "scissors" and user_input == "paper":
        print("The computer won with scissors.")

    elif computer_options[computer_option] == "rock" and user_input == "paper":
        print("You won with paper.")
    elif computer_options[computer_option] == "paper" and user_input == "scissors":
        print("You won with scissors.")
    elif computer_options[computer_option] == "scissors" and user_input == "rock":
        print("You won with rock.")

    else:
        print("It's a tie.")

RockPaperScissors()


            

