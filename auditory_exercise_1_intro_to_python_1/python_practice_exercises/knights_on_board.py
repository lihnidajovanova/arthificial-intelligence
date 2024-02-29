def cannot_capture(board):
    # проверка за секој витез дали може да фати друг витез
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                # проверка за L-форма движење воо сите насоки
                for dx, dy in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
                    x, y = i + dx, j + dy
                    if 0 <= x < 8 and 0 <= y < 8 and board[x][y] == 1:
                        return False
    return True


if __name__ == "__main__":
    board = [[0 for _ in range(8)] for _ in range(8)]
    print("Внесете ги позициите на витезите во формат (ред колона) или 'end' за завршување: ")

    while True:
        position = input()
        if position.lower() == 'end':
            break
        row, column = map(int, position.split())
        board[row][column] = 1

    result = cannot_capture(board)
    print(result)
