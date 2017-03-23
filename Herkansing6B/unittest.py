import unittest
from testfunctions import *

class Test_Model_Answers(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()
		self.app.testing = True

	def test_model_data_exisiting(self):
		response = self.app.post('/easyresult', data = dict(ID="3", verb="go"), follow_redirects=True)
		self.assertTrue("Exists", response.data)

	def test_model_data_notexisting(self):
		response = self.app.post('/easyresult', data = dict(ID="3", verb="hallokidokie"), follow_redirects=True)
		self.assertTrue("Doesn't exist", response.data)

class Test_Model_Result(unittest.Testcase):
	def setUp(self):
		self.app = app.test_client()
		self.app.testing = True

	def test_model_result_equal(self):
		response = self.app.post('/easyresult', data = dict(answer="smoke"), follow_redirects=True)
		self.assertIn("Correct, Score increased by 10", response.data) 

	def test_model_result_diff(self):
		response = self.app.post('/easyresult', data = dict(answer="smokey"), follow_redirects=True)
		self.assertIn("False, Score decreased by 10", response.data) 

if __name__ == '__main__':
	unittest.main()
