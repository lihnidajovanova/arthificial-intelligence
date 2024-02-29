operators = ['+', '-', '*', '/', '**', '//', '%']


def calculator(x, y, operator):
    if operator not in operators:
        return "Invalid operator"

    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == '/':
        return x / y
    elif operator == '**':
        return x ** y
    elif operator == '//':
        return x // y
    elif operator == '%':
        return x % y


if __name__ == '__main__':
    x = float(input("Enter the first number: "))
    operator = input("Enter the operator: ")
    y = float(input("Enter the second number: "))

    result = calculator(x, y, operator)
    print(f"The result is: {result}")
    # print("The result is: ", result)
    # print("The result is: {} {}".format(result, result))
    # print("The result is: %.2f %.2f" % (result, result))
