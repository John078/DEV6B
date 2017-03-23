def test_easyexercise():
    return controller_easy()

def controller_easy():
    return "easy.html"

def test_controller_score():
    testresult = test_model_score()
    return testresult

def test_model_score():
	rightAnswersG1 = [data[0][0],data[1][0]]
	givenAnswersG1 = [answer1.lower(), answer2.lower()]
	score = 0
	for i in range(0, 10):
		if self.givenAnswersG1[i] == self.rightAnswersG1[i]:
			score += 10
	return score
