from flask import Flask, session, flash, redirect, render_template, request
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = "CentralIntel"
mysql = MySQLConnector(app, 'wall')
bcrypt= Bcrypt(app)
import re
email_reg = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/', methods=['GET','POST']) #Homepage
def index():
    if session.get('loggedin') == None: #Check if logged in
        return redirect('/join') #send to login page
    if request.method == 'POST': #see if message was posted or just visiting
        query = "INSERT INTO messages (user_id, message, created_at, updated_at) \
        VALUES (:user_id, :message, NOW(), NOW())"
        data = {
            'user_id': session['loggedin'],
            'message': request.form['postmsg']
        }
        mysql.query_db(query, data)
        return redirect('/')
    else: #display messages and comments as normal
        query = "SELECT concat(first_name, ' ', last_name) AS username FROM users WHERE id = :id LIMIT 1"
        data = {'id': session['loggedin']}
        loggeduser = mysql.query_db(query, data)[0]['username']
        query = "SELECT messages.id AS id, messages.message AS message, date_format(messages.created_at, '%M %D of %Y') AS created,  \
        messages.user_id AS user_id, concat(users.first_name, ' ', users.last_name) AS username\
        FROM messages \
        JOIN users ON messages.user_id = users.id \
        ORDER BY id DESC"
        wallmessages = mysql.query_db(query)
        wallcomments = {}
        for element in wallmessages:
            query = "SELECT comments.user_id AS user_id, comments.comment AS comment, \
            concat(users.first_name, ' ', users.last_name) AS username, date_format(comments.created_at, '%M %D of %Y') AS created \
            FROM comments \
            JOIN users ON comments.user_id = users.id \
            WHERE comments.message_id = :message_id"
            data = {
                'message_id': element['id']
            }
            wallcomments[element['id']] = mysql.query_db(query, data)
        return render_template('index.html', all_messages=wallmessages, all_comments=wallcomments, username=loggeduser)

@app.route('/join') #Login / Register page
def join():
    return render_template('login.html')

@app.route('/login',methods=['POST']) #Login processing
def login():
    query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    data = {'email': request.form['email']}
    user = mysql.query_db(query, data)
    if bcrypt.check_password_hash(user[0]['pw_hash'], request.form['password']):
        session['loggedin'] = user[0]['id']
        return redirect('/')
    else:
        flash("Email or password are incorrect.")
        return redirect('/join')

@app.route('/register', methods=['POST']) #Register processing
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
        pw_hash = None
        query = "SELECT users.id FROM users WHERE email = :email"
        data = {'email': request.form['email']}
        session['loggedin'] = mysql.query_db(query, data)[0]['id']
        return redirect('/')
    else:
        return redirect('/join')

@app.route('/logout', methods=['POST']) #Logout processing
def logout():
    session.pop('loggedin')
    user = None
    query = None
    data = None
    loggeduser = None
    return redirect ('/join')

@app.route('/<message_id>', methods=['POST']) #Comment processing
def comment(message_id):
    query = "INSERT INTO comments (message_id, user_id, comment, created_at, updated_at) \
    VALUES (:message_id, :user_id, :comment, NOW(), NOW())"
    data = {
        'message_id': message_id,
        'user_id': session['loggedin'],
        'comment': request.form['postcmt']
    }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
