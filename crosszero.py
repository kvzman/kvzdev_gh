
matrix = [["-"] * 3 for i in range(3)]
move_num = 0

def hello():
    print("________________________________________________________")
    print("                  Добро пожаловать!                     ")
    print("              Эта игра крестики-нолики                  ")
    print("________________________________________________________")
    print("Чтобы сделать ход, введите координаты X и Y через пробел")
    print("X - номер строки.                                       ")
    print("Y - номер столбца.                                      ")
def print_matrix():
    print()
    print(f"  1 2 3")
    for i in range(3):
        print(f"{i+1} {matrix[i][0]} {matrix[i][1]} {matrix[i][2]}")
    print()

def player_move():
    while True:
        move = input("      Ваш ход  ").split()
        if len(move) != 2:
            print("введите 2 координаты через пробел в диапазоне от 1 до 3")
            continue
        x, y = move

        if not(x.isdigit()) or not(y.isdigit()):
            print("введите 2 координаты через пробел в диапазоне от 1 до 3")
            continue
        x, y = int(x), int(y)

        if 1>x>3 and 1>y>3:
            print("введите 2 координаты через пробел в диапазоне от 1 до 3")
            continue

        if matrix[x-1][y-1] != '-':
            print("Эта клетка занята!")
            continue
        return x-1, y-1

def win_check():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                ((0, 0), (1, 1), (2, 2)),((2, 0), (1, 1), (0, 2)))

    for comb in win_cord:
        win_combo = []
        for i in comb:
            win_combo.append(matrix[i[0]][i[1]])

        if win_combo == ["X", "X", "X"]:
            print_matrix()
            print("Победил крестик!")
            return  True

        if win_combo == ["O", "O", "O"]:
            print_matrix()
            print("Победил нолик!")
            return True

    return False

hello()
while True:
    print_matrix()

    move_num += 1
    if move_num%2 == 1:
        print("Ходит крестик!")
    else:
        print("Ходит нолик!")

    x, y = player_move()

    if move_num % 2 == 1:
        matrix[x][y] = "X"
    else:
        matrix[x][y] = "O"

    if win_check():
        break

    if move_num == 9:
        print("Ничья!")
        break
