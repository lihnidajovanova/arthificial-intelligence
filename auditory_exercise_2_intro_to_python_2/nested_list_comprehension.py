if __name__ == '__main__':
    n = int(input())
    m = int(input())

    elements_matrix = []
    for i in range(0, n):
        # we read the elements as a string, divide the string by a space and convert each element of the list to an int
        elements_row = [int(element) for element in input().split(" ")]
        elements_matrix.append(elements_row)

    # first way - with this you get a list
    result_matrix_A = [elem * 2 for row in elements_matrix for elem in row]
    print(result_matrix_A)

    # second way
    result_matrix_B = [[elements_matrix[i][j] * 2 for j in range(0, m)] for i in range(0, n)]
    print(result_matrix_B)
