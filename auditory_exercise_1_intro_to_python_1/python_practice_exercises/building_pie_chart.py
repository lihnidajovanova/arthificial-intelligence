def pie_chart(data):
    total_frequency = sum(data.values())
    degrees_per_unit = 360 / total_frequency

    result = {}
    for category, frequency in data.items():
        degrees = round(frequency * degrees_per_unit, 1)
        result[category] = degrees

    return result


# pie_chart({ "a": 1, "b": 2 }) ➞ { "a": 120, "b": 240 }
# pie_chart({ "a": 30, "b": 15, "c": 55 }) ➞ { "a": 108, "b": 54, "c": 198 }
# pie_chart({ "a": 8, "b": 21, "c": 12, "d": 5, "e": 4 }) ➞ { "a": 57.6, "b": 151.2, "c": 86.4, "d": 36, "e": 28.8 }

# Примери од задачата
print(pie_chart({"a": 1, "b": 2}))
print(pie_chart({"a": 30, "b": 15, "c": 55}))
print(pie_chart({"a": 8, "b": 21, "c": 12, "d": 5, "e": 4}))
