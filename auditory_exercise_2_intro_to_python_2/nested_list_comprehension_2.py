if __name__ == '__main__':

    n = int(input())
    m = int(input())

    element_matrix = []

    #   for i in range(N):
    #       sublist = []
    #       for j in range(M):
    #           sublist.append(int(input()))
    #       list.append(sublist)

    for i in range(0, n):
        sublist = [int(element) for element in input().split(" ")]
        element_matrix.append(sublist)

    print(element_matrix)

    # element_matrix = [(x * 2, y * 2, z * 2) for (x, y, z) in list]

    # list = [element * 2 for row in element_matrix for element in row]

    element_matrix = [[element * 2 for element in row] for row in element_matrix]

    element_matrix_2 = [[element_matrix[i][j] * 2 for j in range(m)] for i in range(n)]

    print(element_matrix)
    print(element_matrix_2)
