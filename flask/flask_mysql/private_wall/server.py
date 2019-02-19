import re
from flask import Flask, render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL

SCHEMA = "private_wall_demo"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "asdfasdlkfjasdf;ljk"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/wall')
def success():
    if 'user_id' not in session:
        return redirect('/')
    # fetch messageable users
    db = connectToMySQL(SCHEMA)
    query = "SELECT * FROM users WHERE id != %(user_id)s;"
    data = {
        'user_id': session['user_id']
    }
    user_list = db.query_db(query, data)

    # fetch messages
    db = connectToMySQL(SCHEMA)
    query = """SELECT messages.content AS content, users.first_name AS first_name, messages.id AS message_id, messages.created_at AS created_at FROM messages
        JOIN users ON users.id = messages.sender_id
        WHERE receiver_id = %(user_id)s;"""
    data = {
        'user_id': session['user_id']
    }
    messages_list = db.query_db(query, data)

    # fetch current user w/message info
    db = connectToMySQL(SCHEMA)
    query = """SELECT users.first_name AS first_name, COUNT(messages.id) AS message_count FROM users
        JOIN messages ON users.id = messages.sender_id
        WHERE users.id = %(user_id)s;"""
    data = {
        'user_id': session['user_id']
    }
    user_info = db.query_db(query, data)[0]

    return render_template('wall.html',
        users = user_list,
        messages = messages_list,
        user_info = user_info
    )


@app.route('/users/create', methods=['POST'])
def users_new():
    valid = True
    if len(request.form['first_name']) < 2:
        flash("First name must be at least 2 characters")
        valid = False

    if len(request.form['last_name']) < 2:
        flash("Last name must be at least 2 characters")
        valid = False

    if not EMAIL_REGEX.match(request.form['email']):
        flash("Email must be valid")
        valid = False

    if len(request.form['password']) < 8:
        flash("Password must be at least 8 characters")
        valid = False

    if request.form['password'] != request.form['confirm']:
        flash("Passwords must match")
        valid = False

    db = connectToMySQL(SCHEMA)
    validate_email_query = 'SELECT id FROM users WHERE email=%(email)s;'
    form_data = {
        'email': request.form['email']
    }
    existing_users = db.query_db(validate_email_query, form_data)

    if existing_users:
        flash("Email already in use")
        valid = False

    if not valid:
        # redirect to the form page, don't create user
        return redirect('/')

    # hash user's password
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    # create a user and log them in
    db = connectToMySQL(SCHEMA)
    create_query = "INSERT INTO users (first_name, last_name, email, pw_hash) VALUES (%(first)s, %(last)s, %(mail)s, %(pw)s);"
    create_data = {
        'first': request.form['first_name'],
        'last': request.form['last_name'],
        'mail': request.form['email'],
        'pw': pw_hash
    }
    user_id = db.query_db(create_query, create_data)
    session['user_id'] = user_id
    return redirect('/wall')


@app.route('/login', methods=['POST'])
def login():
    db = connectToMySQL(SCHEMA)
    query = "SELECT id, pw_hash FROM users WHERE email=%(email)s;"
    data = {
        "email": request.form['email']
    }
    user_list = db.query_db(query, data)
    if user_list:
        user = user_list[0]
        if bcrypt.check_password_hash(user['pw_hash'], request.form['password']):
            session['user_id'] = user['id']
            return redirect('/wall')

    flash("Email or password incorrect")
    return redirect('/')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/messages/create', methods=['POST'])
def create_message():
    valid = True
    if len(request.form['content']) < 5:
        flash("Message must be at least 5 characters long")
        valid = False
    
    if valid:
        db = connectToMySQL(SCHEMA)
        query = 'INSERT INTO messages (content, sender_id, receiver_id) VALUES(%(content)s, %(sender_id)s, %(receiver_id)s);'
        data = {
            'content': request.form['content'],
            'sender_id': session['user_id'],
            'receiver_id': request.form['receiver_id']
        }
        db.query_db(query, data)
    return redirect('/wall')

@app.route('/messages/<message_id>/delete')
def delete_message(message_id):
    db = connectToMySQL(SCHEMA)
    query = "DELETE FROM messages WHERE messages.id = %(message_id)s;"
    data = {
        'message_id': message_id
    }
    db.query_db(query, data)
    return redirect('/wall')

if __name__ == "__main__":
    app.run(debug=True)