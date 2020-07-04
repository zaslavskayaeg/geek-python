# my_file = open(r'C:\Users\zhuch\PycharmProjects\geek-python\lesson05\data.txt')  # raw
my_file = open(r'data.txt', "w")

if my_file.writable():
    my_file.write("Update\n")

    strings = ["John\n", "Kate\n"]
    my_file.writelines(strings)
else:
    print("Can not write")

my_file.close()