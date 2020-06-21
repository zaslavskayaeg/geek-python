import sys
from lesson04 import my_mod

# print(my_mod.calculate(10))

# print(sys.argv)

try:
    file, user, salary = sys.argv
except ValueError:
    print("invalid args")
    exit()

my_mod.hello(user)
print(my_mod.calculate(int(salary)))
