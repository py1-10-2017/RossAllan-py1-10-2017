from flask import Flask, render_template, request, redirect, session
app =Flask(__name__)
app.secret_key = 'CentralIntel'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form["action"]
        if action == "+2":
            session['times'] += 1
            return redirect("/")
        else:
            session.pop('times')
            return redirect("/")
    else:
        if session.get('times') == None:
            session['times'] = 1
        else:
            session['times'] += 1
        return render_template("index.html")

app.run(debug=True)
