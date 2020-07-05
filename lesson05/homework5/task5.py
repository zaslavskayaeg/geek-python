# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import random

random_list = []

i = 0
n = random.randint(1, 20)
sum_el = 0

while i < n:
    random_list.append(random.randint(1, 1000))
    i += 1

try:
    with open(r'files/task5.txt', "w") as task5:
        for el in random_list:
            print(el, end=' ', file=task5)
except IOError:
    print("Произошла ошибка ввода-вывода!")

try:
    with open(r'files/task5.txt') as task5:
        for string in task5.readlines():
            for el in string.rstrip().split(" "):
                sum_el += int(el)
    print(sum_el)
except IOError:
    print("Произошла ошибка ввода-вывода!")
