import re
from flask import Flask, render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL

SCHEMA = "ft_demo_login_reg"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
INVALID_PASSWORD_REGEX = re.compile(r'^([^0-9]*|[^A-Z]*)$')

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "asdfasdlkfjasdf;ljk"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def success():
    if 'user_id' not in session:
        return redirect('/')
    
    return render_template('success.html')

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

    if INVALID_PASSWORD_REGEX.match(request.form['password']):
        flash("Password must have at least one uppercase character and at least one number")
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
    return redirect('/success')

@app.route('/login', methods=['POST'])
def login():
    print(request.form)
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)