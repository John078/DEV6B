from flask import Flask, render_template
from model import *

model = Model()

class controller:
    def index(self):
        return render_template('Index.html')

    def Ex_easy(self):
        if request.method == 'GET':
            return render_template('easy.html')
        elif request.method == 'POST':
            givenAnswersG1 = model.Inputuser()
            rightAnswersG1 = model.Easyanswers()
            score = model.Result()
            return render_template("easyresult.html", givenAnswersG1=givenAnswersG1, rightAnswersG1=rightAnswersG1, score=score)

    def Ex_medium(self):
        if request.method == 'GET':
            return render_template('medium.html')
        elif request.method == 'POST':
            givenAnswersG1 = model.Inputuser()
            rightAnswersG1 = model.Mediumanswers()
            score = model.Result()
            return render_template("mediumresult.html", givenAnswersG1=givenAnswersG1, rightAnswersG1=rightAnswersG1, score=score)

    def Ex_hard(self):
        if request.method == 'GET':
            return render_template('hard.html')
        elif request.method == 'POST':
            givenAnswersG1 = model.Inputuser()
            rightAnswersG1 = model.Hardanswers()
            score = model.Result()
            return render_template("hardresult.html", givenAnswersG1=givenAnswersG1, rightAnswersG1=rightAnswersG1, score=score)

    def InputuserTest(self):
        if request.method == 'POST':
            input = model.InputuserTest()
            return input

    def ResultTest(self):
        if request.method == 'POST':
            score = model.ResultTest()
            return score

    def Ex_easyTest(self):
        if request.method == 'POST':
            answers = model.Easyanswers()
            return answers

    def Ex_mediumTest(self):
        if request.method == 'POST':
            answers = model.Mediumanswers()
            return answers

    def Ex_hardTest(self):
        if request.method == 'POST':
            answers = model.Hardanswers()
            return answers