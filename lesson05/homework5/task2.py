# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

try:

    with open(r'files/task2.txt', encoding='utf8') as task2:
        i = 0
        for string in task2.readlines():
            i += 1
            print(f"Количество слов в строке {i} = ", len(list(string.split(" "))))

        print(f"Итого строк в файле = {i}")

except IOError:
    print("Произошла ошибка чтения!")
