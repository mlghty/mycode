import requests
import random
import os,time

URL= "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy"

def main():
    data= requests.get(URL).json() 
    length = len(data["results"])-1
    
    for i in range(0,length):
        question = data["results"][i]["question"]
        
        correct_answer = data["results"][i]["correct_answer"]
        all_answers = data["results"][i]["incorrect_answers"]
        all_answers.append(correct_answer)
        random.shuffle(all_answers)
        
        # print(question)
        # print("A: "+all_answers[0])
        # print("B: "+all_answers[1])
        # print("C: "+all_answers[2])
        # print("D: "+all_answers[3])
        
        # that ^ or this v
        
        print(question)
        for answer_index in range(0,4,1):
            print(chr(ord("A") + answer_index) +": "+all_answers[answer_index])
              

        answer = input("Your answer: ")

        if answer.upper() == correct_answer.upper():
            print("Correct!")
        else:
            print("Incorrect. The correct answer is " + correct_answer + "!")
        
        i+=1
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
