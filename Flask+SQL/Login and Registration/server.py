from flask import Flask, session, request, redirect, flash, render_template
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'users')
app.secret_key = "CentralIntel"
import re
email_reg = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    if session.get('loggedin') != None:
        return redirect('/success')
    else:
        return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    success = True
    if len(request.form['fName']) < 2 or (request.form['fName']).isalpha() == False:
        flash("First Name must be at least 2 letters, and only letters.")
        success = False
    if len(request.form['lName']) < 2 or (request.form['lName']).isalpha() == False:
        flash("Last Name must be at least 2 letters, and only letters.")
        success = False
    if not email_reg.match(request.form['email']):
        flash("Email is required and must be valid.")
        success = False
    if len(request.form['password']) < 8:
        flash("Password must be at least 8 characters.")
        success = False
    if request.form['password'] != request.form['pwconfirm']:
        flash("Password and confirmation must match.")
        success = False
    if success == True:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) \
            VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
        data = {
            'first_name': request.form['fName'],
            'last_name': request.form['lName'],
            'email': request.form['email'],
            'pw_hash': pw_hash
        }
        mysql.query_db(query, data)
        query = "SELECT users.id FROM users WHERE email = :email"
        data = {'email': request.form['email']}
        session['loggedin'] = mysql.query_db(query, data)[0]['id']
        return redirect('/success')
    else:
        return redirect('/')

@app.route('/success')
def success():
    query = "SELECT * FROM users WHERE id = :id"
    data = {'id': session['loggedin']}
    user = mysql.query_db(query, data)
    return render_template('success.html', userdata=user)

@app.route('/login', methods=['POST'])
def login():
    query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    data = {'email': request.form['email']}
    user = mysql.query_db(query, data)
    if bcrypt.check_password_hash(user[0]['pw_hash'], request.form['password']):
        session['loggedin'] = user[0]['id']
        return redirect('/success')
    else:
        flash("Email or password are incorrect.")
        return redirect('/')

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('loggedin')
    user = None
    query = None
    data = None
    return redirect('/')

app.run(debug=True)
