#!/usr/bin/env python3
"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""
import random

def main():
    num= random.randint(1,100)

    rounds= 0
    guess= input("Guess a number between 1 and 100\n>") 
    while rounds < 5 and guess != num:

        # COOL CODE ALERT: what is the purpose of the next four lines?
        if guess:
            guess= int(guess)
        else:
            continue

        if guess > num:
            print("Too high!")
            rounds + 1

        if guess < num:
            print("Too low!")
            rounds + 1

        elif guess == num:
            print("Correct!")
            exit()



        guess= input("Guess a number between 1 and 100\n>")   
if __name__ == "__main__":
    main()
