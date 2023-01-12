#!/usr/bin/python3
import random

# rock beats scissors
# scissors beats paper
# paper beats rock

options = ['rock','paper','scissors'] 
print("Welcome to rock paper scissors!")

while True:
    user_input = input("\nEnter either rock, paper or scissors!: ")
    user_input = user_input.lower()
    cpu_input = options[random.randint(0,2)]
    if user_input in options:
        if user_input == cpu_input:
            print("You choose ",user_input, " the computer choose ", cpu_input," its a tie!")
        elif user_input != cpu_input:
            if user_input == "rock" and cpu_input == "scissors":
                print("You choose ",user_input, " the computer choose ", cpu_input," you win!")
            elif user_input == "scissors" and cpu_input =="paper":
                print("You choose ",user_input, " the computer choose ", cpu_input," you win!")
            elif user_input == "paper" and cpu_input =="rock":
                print("You choose ",user_input, " the computer choose ", cpu_input," you win!")
            else:
                print("You choose ",user_input, " the computer choose ", cpu_input," you lose!")  
    
    else:
        print("That is not a valid option!")
        
    continue_playing = input("\nDo you want to keep playing? (y to continue, any key to exit!): ")    


    if continue_playing.lower() != "y":
        print("Exiting game...!")
        exit()
