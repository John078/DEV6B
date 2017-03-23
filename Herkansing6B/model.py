from flask import *
from dbconnect import *

cur = connection.cursor()

class Model:
	def Inputuser(self):
		answer1 = request.form['answer1']
		answer2 = request.form['answer2']
		answer3 = request.form['answer3']
		answer4 = request.form['answer4']
		answer5 = request.form['answer5']
		answer6 = request.form['answer6']
		answer7 = request.form['answer7']
		answer8 = request.form['answer8']
		answer9 = request.form['answer9']
		answer10 = request.form['answer10']
		self.givenAnswersG1 = [answer1.lower(), answer2.lower(), answer3.lower(), answer4.lower(), answer5.lower(), answer6.lower(), answer7.lower(), answer8.lower(), answer9.lower(), answer10.lower()]   
		return self.givenAnswersG1

	def Easyanswers(self):
		cur.execute("SELECT answer FROM gerundinfinitive1")
		data = cur.fetchall()
		self.rightAnswersG1 = [data[0][0],data[1][0],data[2][0],data[3][0],data[4][0],data[5][0],data[6][0],data[7][0],data[8][0],data[9][0]]
		return self.rightAnswersG1

	def Mediumanswers(self):
		cur.execute("SELECT answer FROM gerundinfinitive2")
		data = cur.fetchall()
		self.rightAnswersG1 = [data[0][0],data[1][0],data[2][0],data[3][0],data[4][0],data[5][0],data[6][0],data[7][0],data[8][0],data[9][0]]
		return self.rightAnswersG1

	def Hardanswers(self):
		cur.execute("SELECT answer FROM gerundinfinitive3")
		data = cur.fetchall()
		self.rightAnswersG1 = [data[0][0],data[1][0],data[2][0],data[3][0],data[4][0],data[5][0],data[6][0],data[7][0],data[8][0],data[9][0]]
		return self.rightAnswersG1

	def Result(self):
		score = 0
		for i in range(0, 10):
			if self.givenAnswersG1[i] == self.rightAnswersG1[i]:
				score += 10
		return score