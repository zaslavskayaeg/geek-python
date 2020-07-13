# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
# окончании ввода данных свидетельствует пустая строка.
try:
    with open(r'files/task1.txt', "w", encoding='utf8') as task1:
        while True:
            string = input(
                "Введите строку для записи в файл. Для завершения ввода нажмите Enter. >>> ")
            if string == "":
                break
            print(string, file=task1)
except IOError:
    print("Произошла ошибка ввода-вывода!")
