# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (
# характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя. Пример готовой структуры:
#
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7,# “eд”: “шт.”})
# ]
#
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика
# товара, например название, а значение — список значений-характеристик, например список названий товаров.
#
# Пример:
#
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

goods = []
name = set()
price = set()
quantity = set()
unit = set()

item_info = {}
analytics = {}

i = 0

while True:
    if input("Чтобы добавить новый товар нажмите Enter. Для завершения программы и вывода списка товаров нажмите q. "
             ">>> ") == "q":
        break
    i += 1

    item_info["название"] = input("Введите название товара >>> ")
    item_info["цена"] = input("Введите цену товара >>> ")
    item_info["количество"] = input("Введите количество товара >>> ")
    item_info["ед"] = input("Введите ед.изм. количества >>> ")

    name.add(item_info["название"])
    price.add(item_info["цена"])
    quantity.add(item_info["количество"])
    unit.add(item_info["ед"])

    lst = (i, item_info)
    goods.append(lst)

print(goods)

analytics["название"] = name
analytics["цена"] = price
analytics["количество"] = quantity
analytics["ед"] = unit

print(analytics)
