#!/usr/bin/python3

marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}

  }
#char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk): >").lower()

#char_stat = input("What statistic do you want to know about? (real name, powers, archenemy: >").lower()

#char_name = char_name.title()

loop = True

while loop:
    try:
        char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk): >").lower()
        char_stat = input("What statistic do you want to know about? (real name, powers, archenemy: >").lower()
        print(char_name)
        print(char_stat)
        char_name = char_name.title()
        print( char_name, 's' ,char_stat,' > is: ',  marvelchars[char_name][char_stat])

        print()
        user_continue = input("Do you want to continue to another character? (y/n) >").lower()
        
        if user_continue == "n":
            loop = False
        elif user_continue == "y":
            pass
        else:
            print("Error not a valid option as I am to lazy to check for this case, goodbye..!")
    except:
        print("Probabaly not a valid option that you entered!")
        print("Goodbye!")
        loop = False






