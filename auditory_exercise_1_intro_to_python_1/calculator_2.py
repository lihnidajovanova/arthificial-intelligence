def calculate(a, operator, b):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    elif operator == '//':
        return a // b
    elif operator == '%':
        return a % b
    elif operator == '**':
        return a ** b
    else:
        return 0


if __name__ == "__main__":
    array = input().split(" ")
    print(calculate(int(array[0]), array[1], int(array[2])))
