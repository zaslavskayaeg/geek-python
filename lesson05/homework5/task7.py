# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о
# фирме: название, форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма
# получила убытки, в расчет средней прибыли ее не включать. Далее реализовать список. Он должен содержать словарь с
# фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
# словарь (со значением убытков). Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджер контекста.
import json

company = {}
avg_profit = {}
business = []

try:

    with open(r'files/task7.txt') as task7:

        for string in task7.readlines():
            lst = list(string.replace("\n", "").split(" "))
            i = 0
            if len(lst) == 4:
                profit = round((float(lst[2]) - float(lst[3])), 2)
                company[lst[0]] = profit
        business.append(company)

        i = 0
        S = 0
        for x in company.values():
            if x > 0:
                S += x
                i += 1
        avg_profit = {'average_profit': round(S / i, 2)}
        business.append(avg_profit)

    print(business)
except IOError:
    print("Произошла ошибка чтения!")

with open(r'files/task7_1.txt', 'w') as task7_1:
    json.dump(business, task7_1)
