# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

staff = []
employee = {}

try:
    with open(r'files/task3.txt', encoding='utf8') as task3:
        for string in task3.readlines():
            lst = list(string.replace("\n", "").split(" "))
            if len(lst) == 2:
                employee = {
                    "name": lst[0],
                    "salaries": float(lst[1])
                }
            staff.append(employee)

    # print(staff)

except IOError:
    print("Произошла ошибка чтения!")

print('Фамилии сотрудников с окладом менее 20 тыс.:')
sum_salaries = 0
for empl in staff:
    if empl['salaries'] < 20000.00:
        print(empl['name'])
    sum_salaries = sum_salaries + empl['salaries']

print(f'Средний оклад сотрудника = {sum_salaries / len(staff)}')
