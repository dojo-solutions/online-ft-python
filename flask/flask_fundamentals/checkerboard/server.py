from flask import Flask, render_template, redirect

app = Flask(__name__)

def create_checkerboard(rows=10, cols=10, color1="red", color2="black"):
    board = []
    for i in range(rows):
        # create a new row
        board.append([])
        for j in range(cols):
            # add colors/columns to row
            if i % 2 == 0:
                colors = (color1, color2)
            else:
                colors = (color2, color1)
            # j % 2 is either 1 or 0
            # use the resulting number to access correct index of the colors tuple
            board[i].append(colors[j % 2])
    return board

@app.route('/')
def index():
    board = create_checkerboard()
    return render_template('index.html', checkerboard=board)

@app.route('/<x>')
def rows(x):
    board = create_checkerboard(rows=int(x))
    return render_template('index.html', checkerboard=board)

@app.route('/<x>/<y>')
def rows_cols(x, y):
    board = create_checkerboard(rows=int(x), cols=int(y))
    return render_template('index.html', checkerboard=board)

@app.route('/<x>/<y>/<color1>/<color2>')
def rows_cols_colors(x, y, color1, color2):
    board = create_checkerboard(
        rows = int(x),
        cols = int(y),
        color1 = color1,
        color2 = color2
    )
    return render_template('index.html', checkerboard=board)

if __name__ == "__main__":
    app.run(debug=True)