# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class AbstractClothes(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def quantity(self):
        pass


class Suit(AbstractClothes):

    def __init__(self, name: str, h: float):
        super().__init__(name)
        self._h = h

    @property
    def quantity(self):
        return 2 * self._h + 0.3


class Coat(AbstractClothes):

    def __init__(self, name: str, v: int):
        super().__init__(name)
        self._v = v

    @property
    def quantity(self):
        return self._v / 6.5 + 0.5


class CompositeClothes(AbstractClothes):
    def __init__(self, children: list):
        self.children = children

    @property
    def quantity(self):
        s: float = 0
        for item in self.children:
            s = s + item.quantity
        return s


versace = Suit('versace', 180.0)
dolce_gabbana = Coat('dolce&gabbana', 42)

all_clothes = CompositeClothes([versace, dolce_gabbana])

print(f'{versace.name} = {versace.quantity:.2f} м.')
print(f'{dolce_gabbana.name} = {dolce_gabbana.quantity:.2f} м.')

print(f'Итого материала на всю одежду = {all_clothes.quantity:.2f} м.')
