def transform(list_input):
    return list_input[0], list_input[-1]


if __name__ == "__main__":
    list_input = list(input())
    print(transform(list_input))
