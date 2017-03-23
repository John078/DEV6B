"""
Routes and views for the flask application.
"""
from controller import *
from model import *
from datetime import datetime
from flask import render_template
from Herkansing6B import app
from os import environ

#Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

#create a new instance of the controller class
controller = controller()

@app.route('/')
@app.route('/home')
def home():
    return controller.index()

@app.route('/easy', methods=['GET', 'POST'])
def Ex_easy():
    return controller.Ex_easy()

@app.route('/medium', methods=['GET', 'POST'])
def Ex_medium():
    return controller.Ex_medium()

@app.route('/hard', methods=['GET', 'POST'])
def Ex_hard():
    return controller.Ex_hard()

@app.route('/inputusertest', methods=['GET', 'POST'])
def InputuserTest():
    return controller.InputuserTest()

@app.route('/resulttest', methods=['GET', 'POST'])
def ResultTest():
    return controller.ResultTest()

@app.route('/easytest', methods=['GET', 'POST'])
def Ex_easyTest():
    return controller.Ex_easyTest()

@app.route('/mediumtest', methods=['GET', 'POST'])
def Ex_mediumTest():
    return controller.Ex_mediumTest()

@app.route('/hardtest', methods=['GET', 'POST'])
def Ex_hardTest():
    return controller.Ex_hardTest()