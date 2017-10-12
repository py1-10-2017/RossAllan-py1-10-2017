from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key="CentralIntel"
@app.route('/')
def index():
        return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    if len(request.form["name"]) >= 1 and len(request.form["comment"]) >= 1:
        if len(request.form["comment"]) <= 120:
            global name
            name = request.form["name"]
            global loc
            loc = request.form["loc"]
            global lang
            lang = request.form["lang"]
            global comment
            comment = request.form["comment"]
            return redirect('/results')
        else:
            flash("Comment is too long. Please limit to 120 characters.")
            return redirect('/')
    else:
        flash("Please complete the form.")
        return redirect('/')

@app.route('/results')
def results():
    return render_template("results.html", name=name, loc=loc, lang=lang, comment=comment)
app.run(debug=True)
