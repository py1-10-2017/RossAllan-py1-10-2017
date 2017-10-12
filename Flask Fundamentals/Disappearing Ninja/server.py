from flask import Flask, session, flash, render_template, redirect, request
app = Flask(__name__)
app.secret_key = "CentralIntel"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja', defaults={'color': "blank"})
@app.route('/ninja/<color>')
def ninja(color):
    return render_template("index.html", color = color)

app.run(debug=True)
