from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<word>')
def say(word):
    return f"Hi {word.capitalize()}!"

@app.route('/repeat/<num>/<word>')
def repeat(num, word):
    return word * int(num)

if __name__ == "__main__":
    app.run(debug=True)