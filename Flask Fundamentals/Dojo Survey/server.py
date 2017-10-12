from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
        return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    global name
    name = request.form["name"]
    global loc
    loc = request.form["loc"]
    global lang
    lang = request.form["lang"]
    global comment
    comment = request.form["comment"]
    return redirect('/results')

@app.route('/results')
def results():
    return render_template("results.html", name=name, loc=loc, lang=lang, comment=comment)
app.run(debug=True)
