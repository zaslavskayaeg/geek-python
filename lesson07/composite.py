from abc import ABC, abstractmethod


class AbstractUser(ABC):
    @abstractmethod
    def show_name(self):
        pass


class Person(AbstractUser):

    def show_name(self):
        print(f"it's a person")


class User(AbstractUser):

    def show_name(self):
        print(f"it's a user")


class CompositeUser(AbstractUser):
    def __init__(self, children: list):
        self.children = children

    def show_name(self):
        for item in self.children:
            item.show_name()


a = Person()
b = User()

compositer = CompositeUser([a, b])

compositer.show_name()
