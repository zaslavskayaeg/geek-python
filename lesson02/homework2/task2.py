# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и
# 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
# элементов необходимо использовать функцию input().

input_str = input("Введите элементы списка через запятую >>> ")

exchange_list = input_str.split(",")

print(exchange_list)

for item in range(len(exchange_list)):
    if item + 1 <= len(exchange_list) - 1:
        if item % 2 == 0:
            exchange_list[item], exchange_list[item + 1] = exchange_list[item + 1], exchange_list[item]
print(exchange_list)
