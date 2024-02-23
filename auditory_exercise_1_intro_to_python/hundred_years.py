def calculate_100_years(name, age):
    current_year = 2024
    years_to_100 = 100 - age
    year_100 = current_year + years_to_100
    return f"{name} ќе има 100 години во {year_100}"


name = input("Внесете име: ")
age = int(input("Внесете години: "))

result = calculate_100_years(name, age)
print(result)
