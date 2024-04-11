"""
Idea is to check all possible positions using is_valid() method, and test if one is a mine
with the is_mine() method, which checks if the value is 10 (or random large integer). There are 8 possible directions
that are crucial for the total # of mines surrounding that field.
"""


def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n


def is_mine(r, c):
    return index_matrix[r][c] == 10


def reformat(length, bombs):
    empty = []
    for row in range(length):
        new_row = []
        splitting = " "
        for col in range(length):
            if bombs[row][col] == 10:
                new_row.append('#')
            else:
                new_row.append(str(bombs[row][col]))

        new_row = " ".join(new_row)
        splitting = splitting.join(new_row)
        empty.append(splitting)
    return empty


n = int(input())  # read the first number
matrix = []
index_matrix = []

for i in range(n):
    # read each line
    line = input()
    split = " "
    new_line = []
    row = []
    fields = line.split(' ')
    for field in fields:
        if field == '-':
            new_line.append('0')
            row.append(0)
            # call function
        if field == '':
            new_line.append('')
        if field == "#":
            new_line.append('#')
            row.append(10)

    # used multiple matrices just for testing
    index_matrix.append(row)
    split = split.join(new_line)
    matrix.append(split)

# Update elements inside
for row in range(n):
    for col in range(n):
        counter = 0
        #  N --> (row-1, col)
        if is_valid(row - 1, col):
            if is_mine(row - 1, col):
                counter += 1
        # S --> (row + 1, col)
        if is_valid(row + 1, col):
            if is_mine(row + 1, col):
                counter += 1
        # E --> (row, col+1)
        if is_valid(row, col + 1):
            if is_mine(row, col + 1):
                counter += 1
        # W --> (row, col - 1)
        if is_valid(row, col - 1):
            if is_mine(row, col - 1):
                counter += 1
        # N.E --> (row - 1, col + 1)
        if is_valid(row - 1, col + 1):
            if is_mine(row - 1, col + 1):
                counter += 1
        # N.W --> (row - 1, col - 1)
        if is_valid(row - 1, col - 1):
            if is_mine(row - 1, col - 1):
                counter += 1
        # S.E --> (row + 1, col + 1)
        if is_valid(row + 1, col + 1):
            if is_mine(row + 1, col + 1):
                counter += 1
        # S.W --> (row + 1, col - 1)
        if is_valid(row + 1, col - 1):
            if is_mine(row + 1, col - 1):
                counter += 1
        # Assign value (counter or #)
        if index_matrix[row][col] != 10:
            index_matrix[row][col] = str(counter)

final = reformat(n, index_matrix)
for element in final:
    print(element)
