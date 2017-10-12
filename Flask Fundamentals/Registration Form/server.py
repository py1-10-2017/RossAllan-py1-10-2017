from flask import Flask, session, flash, render_template, redirect, request
app = Flask(__name__)
app.secret_key = "CentralIntel"

import re
email_reg = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

import time

@app.route('/')
def index():
     return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    valid1 = True
    inputtest = ["fname","lname","email","psw","cpsw","birth"]
    for element in inputtest:
        if len(request.form[element]) < 1:
            valid1 = False
            flash(u"Please complete the form.","global")
            break
    if valid1 == True:
        birthdate = time.strptime(request.form['birth'], '%Y-%m-%d')
        valid2 = True
        if request.form["fname"].isalpha() == False or request.form["lname"].isalpha() == False:
            flash(u"Name may only contain letters.","name")
            valid2 = False
        if len(request.form['psw']) < 8:
            flash(u"Password must be at least 8 characters.","password")
            valid2 = False
        if request.form['psw'].isalnum() == False or request.form['psw'].islower() == True:
            flash(u"Password must contain at least 1 number and 1 uppercase character.","password")
            valid2 = False
        if request.form['psw'] != request.form['cpsw']:
            flash(u"Password and Confirm must match.","password")
            valid2 = False
        if not email_reg.match(request.form['email']):
            flash(u"Email must be valid.","email")
            valid2 = False
        if birthdate[0] >= time.localtime()[0] and birthdate[1] >= time.localtime()[1] and birthdate[2] >= time.localtime()[2]:
            flash(u"Birthday must not be on or after today.","birth")
            valid2 = False
        if valid2 == True:
            flash(u"Thanks for submitting your information.","global")
    return redirect('/')

app.run(debug=True)
