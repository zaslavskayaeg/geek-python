# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
# на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса
# Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:

    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


cory = Position('Cory', 'Hampton', 'lawyer', 80000.00, 30000.00)
rosa = Position('Rosa', 'Clarke', 'accountant', 50000.00, 40000.00)

print(f"position = {cory.position}, full_name = {cory.get_full_name()}, total_income = {cory.get_total_income()}")
print(f"position = {rosa.position}, full_name = {rosa.get_full_name()}, total_income = {rosa.get_total_income()}")
