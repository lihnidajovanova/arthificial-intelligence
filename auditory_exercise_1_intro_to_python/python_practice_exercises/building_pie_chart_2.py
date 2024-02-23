if __name__ == "__main__":
    data = {}
    total_frequency = 0

    while True:
        try:
            line = input("Внесете категорија и фреквенција (внесете 'end' за да завршите):\n")
            if line == "end":
                break
            category, frequency = line.split()
            frequency = int(frequency)
            data[category] = frequency
            total_frequency += frequency
        except ValueError:
            print("Invalid Input. Try again.")

    degree_per_unit = 360 / total_frequency

    result = {}
    for category, frequency in data.items():
        degrees = round(frequency * degree_per_unit, 1)
        result[category] = degrees

    print(result)