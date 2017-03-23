import unittest
import os
import flask
from model import *
from controller import controller
from Herkansing6B import views
from Herkansing6B import app
import tempfile

modelClass = Model()


class Test_Model_InputuserTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    #test InputuserTest function in combination with the /inputusertest route (source: views.py)
    def test_model_InputuserTest(self):
        self.assertTrue(modelClass.InputuserTest("A","B","C","D","E","f","g","h","i","j"), ["a","b","c","d","e","f","g","h","i","j"])

class Test_Model_ResultTest(unittest.TestCase): 
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    #test ResultTest function in combination with the /resulttest route (source: views.py)
    def test_model_ResultTest_score_is_100(self):
        self.assertTrue(modelClass.ResultTest(["a","b","c","d","e","f","g","h","i","j"], ["a","b","c","d","e","f","g","h","i","j"]), 100)

    #test ResultTest function in combination with the /resulttest route (source: views.py)
    def test_model_ResultTest_score_is_60(self):
        self.assertTrue(modelClass.ResultTest(["a","b","c","d","e","f","d","c","b","a"], ["a","b","c","d","e","f","g","h","i","j"]), 60)

class Test_Model_Easyanswers(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    #test Easyanswers function in combination with the /easytest route (source: views.py)
    def test_model_Easyanswers(self):
        response = self.app.post('/easytest', data = dict(), follow_redirects=True)
        self.assertTrue(["to smoke", "laughing", "to go", "help", "to quit", "shouting", "to cook", "to open", "to change", "smoking"], response.data)

class Test_Model_Mediumanswers(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    #test Mediumanswers function in combination with the /mediumtest route (source: views.py)
    def test_model_Mediumanswers(self):
        response = self.app.post('/mediumtest', data = dict(), follow_redirects=True)
        self.assertTrue(["getting", "stealing", "reading", "to go", "going", "to speak", "working", "to talk", "going", "playing"], response.data)
       
class Test_Model_Hardanswers(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    #test Hardanswers function in combination with the /hardtest route (source: views.py)
    def test_model_Hardanswers(self):
        response = self.app.post('/hardtest', data = dict(), follow_redirects=True)
        self.assertTrue(["to help", "to do", "to become", "becoming", "to travel", "to be", "to speak", "seeing", "to call", "to go"], response.data) 
        
if __name__ == '__main__':
	unittest.main()