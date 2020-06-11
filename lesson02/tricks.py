# 1 Объединение списков
nums = [
    [1, 2, 3],
    [4, 5, 6],
]

joined = sum(nums, [])

print(joined)

# 2 Удление дубликатов в списке
unique = [1, 2, 3, 3]
unique = list(set(unique))

print(unique)

# 3 Обмен значениями переменных при помощи кортежей
# a = 10
# b = 20
a, b = 10, 20
a, b = b, a

print(f"a = {a}, b = {b}")

# 4 Поиск максимального значения с помощью аргумента key
total = [1, 2, 1, 3, 1, 3]
print(
    max(set(total), key=total.count)
)

# 5 вывод значений списка в виде отдельных элементов

print(*total, end='', sep='-')
