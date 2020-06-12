# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и через dict.

Err_txt = "Вы ввели некорректное значение!"

# 3.1 Решениe через list
seasons = ("зима", "весна", "лето", "осень")
months = tuple({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12})

# while True:
#     input_months = input("Введите порядковый номер месяца от 1 до 12. Для завершения введите q. >>>")
#     if input_months == "q":
#         break
#     try:
#         input_months = int(input_months)
#         i = months.index(input_months)
#         if i < 2 or i == 11:
#             print(i, seasons[0])
#         elif i < 5:
#             print(i, seasons[1])
#         elif i < 8:
#             print(i, seasons[2])
#         else:
#             print(i, seasons[3])
#
#     except ValueError:
#         print(Err_txt)

# 3.2 Решениe через dict
seasons_dict = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень',
                10: 'осень', 11: 'осень', 12: 'зима'}
while True:
    input_months = input("Введите порядковый номер месяца от 1 до 12. Для завершения введите q. >>>")
    if input_months == "q":
        break
    try:
        input_months = int(input_months)
        print(seasons_dict.get(input_months, Err_txt))
    except ValueError:
        print(Err_txt)
