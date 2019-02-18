from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL

SCHEMA = "c_and_r_pets_demo"

app = Flask(__name__)

@app.route('/')
def index():
    db = connectToMySQL(SCHEMA)
    query = "SELECT * FROM pets;"
    pets_list = db.query_db(query)
    return render_template('index.html', pets=pets_list)

@app.route('/process', methods=['POST'])
def process():
    db = connectToMySQL(SCHEMA)
    query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES(%(name)s, %(type)s, NOW(), NOW());"
    data = {
        "name": request.form['name'],
        "type": request.form['type']
    }
    db.query_db(query, data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)