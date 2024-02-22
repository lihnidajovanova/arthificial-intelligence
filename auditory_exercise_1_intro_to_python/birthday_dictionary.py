birthday_dict = {
    "Ana": "13/03/1999",
    "Marija": "17/01/1991",
    "Stefan": "11/08/1864",
    "Aleksandar": "25/10/1992"
}

print("Dobredojdovte do recniot za rodendeni. Nie gi znaeme rodendenite na: ")
print("\n".join(birthday_dict.keys()))

print("Koj rodenden e potrebno da se prebara?")
user = input()

birthday = birthday_dict[user]
print(f"Rodendenot na {user} e na {birthday}")
