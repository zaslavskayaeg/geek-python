# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее
# сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

rev = int(input("Введите выручку фирмы >>> "))
exp = int(input("Введите издержки фирмы >>> "))
pr = rev - exp

if pr > 0:
    print("Прибыль = {}; Финансовый результат - прибыль".format(pr))
    ren = pr / rev
    print("Рентабельность выручки = {:.2f}".format(ren))

    empl_num = int(input("Введите численность сотрудников фирмы >>> "))
    empl_pr = pr / empl_num
    print("Прибыль фирмы в расчете на одного сотрудника = {:.2f}".format(empl_pr))

elif pr < 0:
    print("Прибыль = {:.2f}; Финансовый результат - убыток".format(pr))

else:
    print("Выручка равна издержкам. Финансовый результат не определен.")