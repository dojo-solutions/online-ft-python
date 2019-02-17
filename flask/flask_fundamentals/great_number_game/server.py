import random
from flask import Flask, redirect, render_template, session, request

app = Flask(__name__)
app.secret_key = "asdflkjwefslkdjfa;lkjdsf"

@app.route('/')
def index():
    if "random_number" not in session:
        session['random_number'] = random.randint(1, 100)
    if "num_guesses" not in session:
        session['num_guesses'] = 0

    game_info = {
        "message": None,
        "css_class": None
    }

    if "guess" not in session:
        game_info["message"] = "Take a guess!"
        game_info['css_class'] = "yellow"
    elif session['num_guesses'] > 4:
        game_info["message"] = "You lose!"
        game_info["css_class"] = "red"
    elif session["guess"] > session["random_number"]:
        game_info["message"] = "Too high!"
        game_info['css_class'] = "red"
    elif session["guess"] < session["random_number"]:
        game_info["message"] = "Too low!"
        game_info['css_class'] = "red"
    else:
        game_info["message"] = f"{session['random_number']} was the number!"
        game_info['css_class'] = "green"
    return render_template('index.html', info=game_info)

@app.route('/process', methods=["POST"])
def process():
    session['guess'] = int(request.form['guess'])
    session["num_guesses"] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)