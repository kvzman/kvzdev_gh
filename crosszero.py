# print('  1 2 3\n1 - - -\n2 - - -\n3 - - -')

# input("ход первого игрока")
# input("ход второго игрока")

matrix = [
    [' ', 1, 2, 3],
    [1, "-", "-", "-"],
    [2, "-", "-", "-"],
    [3, "-", "-", "-"],
]
def print_matrix():
    for row in matrix:
        for el in row:
            print(el, end=" ")
        print()

def cross(pl1_row, pl1_el):
    if matrix[pl1_row][pl1_el] == "-":
        matrix[pl1_row][pl1_el] = "X"
    print_matrix()
    return matrix

def circle(pl2_row, pl2_el):
    if matrix[pl2_row][pl2_el] == "-":
        matrix[pl2_row][pl2_el] = "O"
    print_matrix()
    return matrix
print(matrix)

def win_cross():
    if matrix[1][1] == "X" and matrix[1][2] == "X" and matrix[1][3] == "X":
        print("первый игрок победил")
    elif matrix[2][1] == "X" and matrix[2][2] == "X" and matrix[2][3] == "X":
        print("первый игрок победил")
    elif matrix[3][1] == "X" and matrix[3][2] == "X" and matrix[3][3] == "X":
        print("первый игрок победил")
    elif matrix[1][1] == "X" and matrix[2][1] == "X" and matrix[3][1] == "X":
        print("первый игрок победил")
    elif matrix[1][2] == "X" and matrix[2][2] == "X" and matrix[3][2] == "X":
        print("первый игрок победил")
    elif matrix[1][3] == "X" and matrix[2][3] == "X" and matrix[3][3] == "X":
        print("первый игрок победил")
    elif matrix[1][1] == "X" and matrix[2][2] == "X" and matrix[3][3] == "X":
        print("первый игрок победил")
    elif matrix[1][3] == "X" and matrix[2][2] == "X" and matrix[3][1] == "X":
        print ("первый игрок победил")


for i in range(9):
    player_1 = input("ход первого игрока")
    pl1_row = int(player_1[0])
    pl1_el = int(player_1[1])
    cross(pl1_row, pl1_el)
    win_cross()

    player_2 = input("ход второго игрока")
    pl2_row = int(player_2[0])
    pl2_el = int(player_2[1])
    circle(pl2_row, pl2_el)





