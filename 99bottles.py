#!/usr/bin/python3


def bottles(num):
    for bottle in range(0,num):
        print(num, " bottles of beer on the wall!")
        print(num," bottles of beer on the wall!",num," bottles of beer!", "You take one down, pass it around!")
        num -= 1


def main():
    input_bottles = input("How many bottles today?")
    try:
        bottles(int(input_bottles))
    except:
        print("Not valid must be a integer!")

if __name__ == "__main__":
    main()
