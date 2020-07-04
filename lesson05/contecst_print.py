with open('data.txt', "w") as printable:
    strings = ["John", "Kate"]

    for x in strings:
        print(x, file=printable)
