import random
from datetime import datetime
from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "asldkjfa;lskdjf"

@app.route('/')
def index():
    if not 'activities' in session:
        session['activities'] = []
        
    if not 'gold' in session:
        session['gold'] = 0
    return render_template('index.html')

@app.route('/process', methods=["POST"])
def process():
    location_map = {
        'farm': random.randint(10, 20),
        'cave': random.randint(5, 10),
        'house': random.randint(2, 5),
        'casino': random.randint(-50, 50),
    }
    curr_gold = location_map[request.form['location']]

    activity = {}
    if curr_gold >= 0:
        activity['css_class'] = "green"
        activity['content'] = f"Earned {curr_gold} golds from the {request.form['location']}! ({datetime.now().strftime('%Y/%m/%d %I:%M:%S %p')})"
    else:
        activity['css_class'] = "red"
        activity['content'] = f"Lost {curr_gold * -1} golds from the {request.form['location']}! ({datetime.now().strftime('%Y/%m/%d %I:%M:%S %p')})"

    session['activities'].insert(0, activity)
    session['gold'] += curr_gold

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)