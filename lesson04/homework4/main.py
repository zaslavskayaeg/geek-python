# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

import sys
from lesson04.homework4 import task1

try:
    file, hourly_rate, man_hours, bonus = sys.argv
except ValueError:
    print("invalid args")
    exit()

print(task1.salary_func(int(hourly_rate), int(man_hours), int(bonus)))