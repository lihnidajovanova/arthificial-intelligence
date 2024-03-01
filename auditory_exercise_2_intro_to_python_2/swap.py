def swap(list):
    return [(item2, item1) for item1, item2 in list]


if __name__ == "__main__":
    print(swap([('a', 1), ('b', 2), ('c', 3)]))
