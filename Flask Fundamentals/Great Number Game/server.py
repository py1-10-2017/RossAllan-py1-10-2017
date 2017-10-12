from flask import Flask, request, redirect, session, render_template
import random
app = Flask(__name__)
app.secret_key = 'CentralIntel'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form["action"] == "guess":
            if int(request.form["guess"]) == session['rannum']:
                session['result'] = "correct"
            elif int(request.form["guess"]) > session['rannum']:
                session['result'] = "high"
            elif int(request.form["guess"]) < session['rannum']:
                session['result'] = "low"
        else:
            session.pop('result')
            session['rannum'] = random.randrange(1,101)
        return redirect("/")
    else:
        if session.get('rannum') == None:
            session['rannum'] = random.randrange(1,101)
        return render_template("index.html")

app.run(debug=True)
