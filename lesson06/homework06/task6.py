# 6. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
# draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery:
    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки.\n")


class Pen(Stationery):
    def __init__(self, title: str):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки. Ручка.\n")


class Pencil(Stationery):
    def __init__(self, title: str):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки. Карандаш.\n")


class Handle(Stationery):
    def __init__(self, title: str):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки. Маркер.\n")


liner = Stationery("liner")
pencil = Pencil("pencil")
handle = Handle("handle")
pen = Pen("pen")

pencil.draw()
liner.draw()
handle.draw()
pen.draw()
