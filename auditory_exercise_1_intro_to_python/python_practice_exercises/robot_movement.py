import math


def calculate_distance(moves):
    x, y = 0, 0

    for move in moves:
        direction, steps = move.split()
        # direction, steps = move[0], move[1]
        steps = int(steps)

        if direction == "UP":
            y += steps
        elif direction == "DOWN":
            y -= steps
        elif direction == "LEFT":
            x -= steps
        elif direction == "RIGHT":
            x += steps

    euclidean_distance = math.sqrt(x ** 2 + y ** 2)
    manhattan_distance = abs(x) + abs(y)

    return euclidean_distance, manhattan_distance


moves = []
while True:
    move = input("Enter your moves (enter 'END' for end):\n")
    if move == 'END':
        break
    moves.append(move)

euclidean, manhattan = calculate_distance(moves)

print(f"Euclidean distance: {euclidean:.2f}")
print(f"Manhattan distance: {manhattan:}")
