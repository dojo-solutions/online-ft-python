def create_checkerboard2(rows=10, cols=10, color1="red", color2="black"):
    board = []
    for i in range(rows):
        # create a new row
        board.append([((color1, color2), (color2, color1))[i % 2][j % 2] for j in range(cols)])
    return board

# print(create_checkerboard2())

def create_checkerboard3(rows=10, cols=10, color1="red", color2="black"):
    return [[((color1, color2), (color2, color1))[i % 2][j % 2] for j in range(cols)] for i in range(rows)]

print(create_checkerboard3())