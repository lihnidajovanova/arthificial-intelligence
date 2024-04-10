if __name__ == "__main__":
    birthday_dict = {
        "Ana": "13/03/1999",
        "Marija": "17/01/1991",
        "Stefan": "11/08/1864",
        "Aleksandar": "25/10/1992"
    }

    print("Dobredojdovte do recniot za rodendeni. Nie gi znaeme rodendenite na: ")
    for key in birthday_dict.keys():
        print(key)

    name = input("Koj rodenden e potrebno da se prebara?\n")
    print("Rodendenot na " + name + " e " + birthday_dict[name])
