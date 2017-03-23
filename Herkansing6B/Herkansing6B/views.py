"""
Routes and views for the flask application.
"""
from controller import *
from datetime import datetime
from flask import render_template
from Herkansing6B import app

@app.route('/')
@app.route('/home')
def home():
    return controller.index()

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/easy', methods=['GET', 'POST'])
def Ex_easy():
    return controller.Ex_easy()

@app.route('/medium', methods=['GET', 'POST'])
def Ex_medium():
    return controller.Ex_medium()

@app.route('/hard', methods=['GET', 'POST'])
def Ex_hard():
    return controller.Ex_hard()


