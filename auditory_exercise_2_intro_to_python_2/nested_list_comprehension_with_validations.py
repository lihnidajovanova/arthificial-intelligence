def multiply_element(element, i, n):
    if i < n / 2:
        return element * 2
    else:
        return element * 3


if __name__ == "__main__":
    n = int(input())
    m = int(input())

    elements_matrix = []

    for i in range(0, n):
        # we read the elements as a string, divide the string by a space and convert each element of the list to an int
        elements_row = [int(element) for element in input().split(" ")]
        elements_matrix.append(elements_row)

    result_matrix = [[multiply_element(elements_matrix[i][j], i, n) for j in range(0, m)] for i in range(0, n)]
    print(result_matrix)
