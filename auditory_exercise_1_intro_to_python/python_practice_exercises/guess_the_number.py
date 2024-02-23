def guess_number():
    start = 1
    end = 1000000000

    while True:
        guess = (start + end) // 2
        response = input(f"Дали вашиот број е {guess}? (да/поголем/помал):")

        if response.lower() == "да":
            print(f"Бројот е {guess}.")
            break
        elif response.lower() == "поголем":
            start = guess + 1
        elif response.lower() == "помал":
            end = guess - 1


if __name__ == '__main__':
    guess_number()
