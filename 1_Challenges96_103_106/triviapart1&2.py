from flask import Flask,request
from flask import redirect
from flask import render_template

import requests
import random
import html

app = Flask(__name__)


answers_dict = {}

@app.route('/')
def get_question():
    URL = "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy"
    response = requests.get(URL)
    data = response.json()['results'][0]

        
    question =  html.unescape(data['question'])
    
    correct_answer = data["correct_answer"]
    all_answers = data["incorrect_answers"]
    all_answers.append(correct_answer)
    
    answers_dict[question] = correct_answer
    
    for i in range(0,len(all_answers)):
        all_answers[i] = html.unescape(all_answers[i])
        
    random.shuffle(all_answers)
    

    return render_template('question.html', question=question,answers=all_answers)


@app.route('/validate',methods = ['POST'])
def validate_answer():
    global answers_dict
    
    data = request.form

    question = request.form['question']
    answer = request.form['answer']
    print(answers_dict[question])
    print(answer)
    if answers_dict[question] == answer:
        print("wrong!")
        return question_correct_or_incorrect_page("Correct!","text-success")
    else:
        return question_correct_or_incorrect_page("Incorrect!","text-danger")

    

@app.route('/correct')
def question_correct_or_incorrect_page(user_input,color):
    return render_template('splash.html',correct_or_incorrect=user_input,color=color),{"Refresh": "3; /"}


if __name__ == '__main__':
    app.run(debug=True)