from flask import Flask, session, flash, render_template, redirect, request
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friends')
app.secret_key = "CentralIntel"
import re
email_reg = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)

@app.route('/add', methods=['POST'])
def add():
    if email_reg.match(request.form['email']) and request.form['fName'] != '' and request.form['lName'] != '':
        query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
        data = {
            'first_name': request.form['fName'],
            'last_name': request.form['lName'],
            'email': request.form['email']
        }
        mysql.query_db(query, data)
    else:
        flash("All forms must be complete and email must be valid.")
    return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
    query = "SELECT * FROM friends WHERE id = :id"
    data = {'id': id}
    global friend_info
    friend_info = mysql.query_db(query, data)
    return render_template('edit.html', friend=friend_info)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    def emailtemp():
        if email_reg.match(request.form['email']):
            return request.form['email']
        else:
            return friend_info[0]['email']
    def fnametemp():
        if request.form['fName'] != "":
            return request.form['fName']
        else:
            return friend_info[0]['first_name']
    def lnametemp():
        if request.form['lName'] != "":
            return request.form['lName']
        else:
            return friend_info[0]['last_name']
    query = "UPDATE friends \
    SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = NOW() \
    WHERE id = :id"
    data = {
        'email': emailtemp(),
        'first_name': fnametemp(),
        'last_name': lnametemp(),
        'id': id
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def delete(id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
