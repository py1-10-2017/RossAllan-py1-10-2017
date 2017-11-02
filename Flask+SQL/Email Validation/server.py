from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'emailsdb')
import re
email_reg = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app.secret_key="CentralIntel"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process',methods=['POST'])
def process():
    if email_reg.match(request.form['email']):
        emailtemp = request.form['email'].split("@")
        query = "INSERT INTO emails (user, domain, created_at) VALUE(:user, :domain, NOW())"
        data = {
            'user': emailtemp[0],
            'domain': emailtemp[1]
        }
        mysql.query_db(query, data)
        return redirect('/success')
    else:
        flash("Email must be valid!")
        return redirect('/')

@app.route('/success')
def success():
    query = "SELECT * FROM emails"
    emails = mysql.query_db(query)
    return render_template('success.html', all_emails=emails)

@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    query = "DELETE FROM emails WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/success')

app.run(debug=True)
