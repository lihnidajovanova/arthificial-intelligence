number = int(input("Внесете број: "))
if number % 2 == 0:
    print("Парен")
    if number % 4 == 0:
        print("Делив со 4")
else:
    print("Непарен")
