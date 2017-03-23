from flask import Flask, render_template
from model import *

model = Model()

class controller:
    def index():
        return render_template('Index.html')

    def Ex_easy():
        if request.method == 'GET':
            return render_template('easy.html')
        elif request.method == 'POST':
            givenAnswersG1 = model.Inputuser()
            rightAnswersG1 = model.Easyanswers()
            score = model.Result()
            return render_template("easyresult.html", givenAnswersG1=givenAnswersG1, rightAnswersG1=rightAnswersG1, score=score)

    def Ex_medium():
        if request.method == 'GET':
            return render_template('medium.html')
        elif request.method == 'POST':
            givenAnswersG1 = model.Inputuser()
            rightAnswersG1 = model.Mediumanswers()
            score = model.Result()
            return render_template("mediumresult.html", givenAnswersG1=givenAnswersG1, rightAnswersG1=rightAnswersG1, score=score)

    def Ex_hard():
        if request.method == 'GET':
            return render_template('hard.html')
        elif request.method == 'POST':
            givenAnswersG1 = model.Inputuser()
            rightAnswersG1 = model.Hardanswers()
            score = model.Result()
            return render_template("hardresult.html", givenAnswersG1=givenAnswersG1, rightAnswersG1=rightAnswersG1, score=score)
