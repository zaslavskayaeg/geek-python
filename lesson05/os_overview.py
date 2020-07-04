import os

if os.path.exists('data.txt'):
    os.remove('data.txt')

currend_dir = "."
files = os.listdir(currend_dir)

for x in files:
    print((os.path.split(x)))
    # print(os.path.isdir(f"./{x}"))
    # print(os.path.dirname("/etc/hosts"))

print(os.path.split(r"/etc/hosts"))
print(files)

print(os.path.join(r'/etc/hosts', "file", "hop", "1.txt"))
