# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый
# текстовый файл.

try:
    with open(r'files/task4.txt') as task4:
        i = 0
        try:
            with open(r'files/task4_1.txt', "w") as task4_1:
                for string in task4.readlines():
                    print(string.replace('One', 'Один').replace('Two', 'Два').replace('Three', 'Три').replace('Four',
                                                                                                              'Четыре'),
                          end="", file=task4_1)
        except IOError:
            print("Произошла ошибка ввода-вывода!")

except IOError:
    print("Произошла ошибка чтения!")
