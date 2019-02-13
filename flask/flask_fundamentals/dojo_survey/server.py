from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "a;slkdjfa;slkdjfksdjlfkaj"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/process', methods=["POST"])
def process():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['favorite_language'] = request.form['favorite_language']
    session['radio'] = request.form['radio']
    session['comment'] = request.form['comment']

    # deal with checkboxes
    checkbox_names = ['check1', 'check2', 'check3']
    checkbox_answers = []
    for name in checkbox_names:
        if name in request.form:
            checkbox_answers.append(request.form[name])
    session['check'] = checkbox_answers
    return redirect('/result')

if __name__ == "__main__":
    app.run(debug=True)