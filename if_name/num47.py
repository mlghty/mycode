import html

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

question = trivia['question']
correct_answer=trivia['correct_answer']
other_answers=trivia['incorrect_answers']
all_answers = other_answers
all_answers.append(correct_answer)
print(question)

#print( html.escape(all_answers),sep='\n')
for i in range(len(all_answers)):
    print("  ",str(i+1)+". "+html.unescape(all_answers[i]))

while True:
    user_input = input("Enter you answer:(1,2,3,4)  >")

    options = ["1","2","3","4"]
    if user_input in options:
        test = all_answers[int(user_input)-1]
        if test == correct_answer:
            print("That is correct!")
            quit()
        else:
            print("That is incorrect!")
            try_again = input("Try again? (y to continute, any key to exit!) :>")
            if try_again.lower() != "y":
                quit()



    else:
        print("Not a valid option!")
        try_again = input("Try again? (y to continute, any key to exit!) :>")
        if try_again.lower() != "y":
             quit()

