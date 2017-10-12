from flask import Flask, render_template, session, request, redirect
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key="CentralIntel"

@app.route("/")
def index():
    if session.get('gold') == None:
        session['gold'] = 0
    if session.get('history') == None:
        session['history'] = []
    return render_template("index.html")

@app.route("/process_money", methods=['POST'])
def process_money():
    time = datetime.now()
    if request.form['action'] == "farm":
        gain = True
        roll = random.randrange(10,21)
    elif request.form['action'] == "cave":
        gain = True
        roll = random.randrange(5,11)
    elif request.form['action'] == "house":
        gain = True
        roll = random.randrange(2,6)
    elif request.form['action'] == "casino":
        if random.randrange(1,3) == 1:
            gain = True
        else:
            gain = False
        roll = random.randrange(0,51)
    if gain == True:
        session['gold'] += roll
        session['history'].append({"type":"gain","result":"Gained "+str(roll)+" gold at the "+request.form['action']+"! ("+str(time.strftime('%x %I:%M %p'))+")"})
    else:
        session['gold'] -= roll
        session['history'].append({"type":"loss","result":"Lost "+str(roll)+" gold at the "+request.form['action']+"! ("+str(time.strftime('%x %I:%M %p'))+")"})
    return redirect("/")

app.run(debug=True)
