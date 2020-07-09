# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.

import time

directions = ['north', 'south', 'east', 'west']


class Car:

    def __init__(self, name: str, color: str, speed: int, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        start_time = time.localtime()
        print(f"Car {self.name} {self.color} started at ", time.strftime("%H:%M:%S", start_time), "\n")
        return start_time

    def stop(self):
        stop_time = time.localtime()
        print(f"Car {self.name} {self.color} stopped at ", time.strftime("%H:%M:%S", stop_time), "\n")
        return stop_time

    def turn(self, direction):
        print(f"Car {self.name} {self.color} turned {direction}")

    def show_speed(self):
        print(f"Car's {self.name} {self.color} speed is {self.speed} km/h\n")


class TownCar(Car):
    def __init__(self, name: str, color: str, speed: int):
        super().__init__(name, color, speed, False)

    def show_speed(self):
        if self.speed <= 60:
            print(f"Car's {self.name} {self.color} speed is {self.speed} km/h\n")
        else:
            print(
                f"Car's {self.name} {self.color} speed is {self.speed} km/h\nMAXIMUM SPEED WARNING! Max speed = 60 km/h.\n")


class SportCar(Car):
    def __init__(self, name: str, color: str, speed: int):
        super().__init__(name, color, speed, False)


class WorkCar(Car):
    def __init__(self, name: str, color: str, speed: int):
        super().__init__(name, color, speed, False)

    def show_speed(self):
        if self.speed <= 40:
            print(f"Car's {self.name} {self.color} speed is {self.speed} km/h\n")
        else:
            print(
                f"Car's {self.name} {self.color} speed is {self.speed} km/h\nMAXIMUM SPEED WARNING! Max speed = 40 km/h.\n")


class PoliceCar(Car):
    def __init__(self, name: str, color: str, speed: int):
        super().__init__(name, color, speed, True)


# 5. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

my_car1 = TownCar("Honda", "blue", 60)
my_car2 = TownCar("Toyota", "white", 90)
police_car1 = PoliceCar("Lada", "white", 120)
sport_car1 = SportCar("Nissan Skyline", "blue", 170)
work_car1 = WorkCar("VOLVO FH", "silver", 20)

my_car1.go()
time.sleep(1)

my_car2.go()
time.sleep(2)

my_car1.turn(directions[3])
my_car1.show_speed()

my_car2.show_speed()

my_car1.stop()

police_car1.go()
police_car1.show_speed()
print(f"{police_car1.name} is a police car = {police_car1.is_police}")

print(f"{work_car1.name} сolor - {work_car1.color}")
work_car1.show_speed()
work_car1.speed = 70
work_car1.show_speed()

sport_car1.go()
time.sleep(2)
sport_car1.show_speed()
sport_car1.stop()
