# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный,
# желтый,
# зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
# завершать скрипт.
from time import sleep


class TrafficLight:

    def __init__(self, h1, h2, h3):
        self.__color = ""
        self.colors = {"": 0, "red": h1, "yellow": h2, "green": h3}

    def running(self):
        """
        переключение светофора
        Выполняет задержку и возвращает следующий сигнал светофора
        :return: сигнал светофора.
        :type: str
        """
        sleep(self.colors[self.__color])
        if self.__color == "":
            self.__color = "red"
        elif self.__color == "red":
            self.__color = "yellow"
        elif self.__color == "yellow":
            self.__color = "green"
        elif self.__color == "green":
            self.__color = "red"

        return f"{self.__color}"


tl1 = TrafficLight(7, 2, 11)

i = 1

n = int(input("Введите кол-во переключений светофора>>> "))

while i <= n:
    print(tl1.running())
    i += 1
