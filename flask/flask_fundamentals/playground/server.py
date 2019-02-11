from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('play.html', number=3, color="lightblue")

@app.route('/play/<num>')
def play_num(num):
    return render_template('play.html', number=int(num), color="lightblue")

@app.route('/play/<num>/<color>')
def play_all(num, color):
    return render_template('play.html', number=int(num), color=color)

if __name__ == "__main__":
    app.run(debug=True)