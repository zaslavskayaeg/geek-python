# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
# while и арифметические операции.

number = input("ведите число >>> ")
i = 0
max_num = 0
while i < len(number):

    if max_num < int(number[i]):
        max_num = int(number[i])
    i += 1

print("Самая большая цифра в числе = %d" % max_num)
