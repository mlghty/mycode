#!/usr/bin/python3

def farm():
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
    

    for animal in farms['NE Farm']['agriculture']:
        print(animal)

        
    print()

    options = ["ne farm","w farm","se farm"]
    user_input_farm = input("Choose which farm to see its agriculture (NE Farm, W Farm, SE Farm) :")
    
    if user_input_farm.lower() in options:
        print("This is, " , user_input_farm, " agriculture!")
        print(farms['name'][user_input_farm.title()]['agriculute'])


        




def main():
    farm()

if __name__ == "__main__":
    main()
