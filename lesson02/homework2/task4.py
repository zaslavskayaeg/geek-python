# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

input_str = input("Введите строку >>> ")

words = list(input_str.split(" "))

for word in words:
    print(words.index(word), word[:10])
