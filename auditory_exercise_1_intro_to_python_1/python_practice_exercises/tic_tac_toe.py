def tic_tac_toe(board):
    for i in range(3):
        # проверка за победа по редови
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != 'E':
            return board[i][0]
        # проверка за победа по колони
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != 'E':
            return board[0][i]

    # проверка за победа по дијагонали
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 'E':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 'E':
        return board[0][2]

    # проверка за нерешено
    for row in board:
        if 'E' in row:
            return "Continue"

    # ако нема празни полоња, тогаш е нерешено
    return "Draw"


def read_board():
    board = []
    for i in range(3):
        row = input(f"Внесете ја редицата број {i + 1} од 3 елементи (X, O, E): ").split()
        board.append(row)
    return board


board = read_board()
result = tic_tac_toe(board)
print(f"Резултат: {result}")
