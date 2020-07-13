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


john = Person()
arthur = User()

john.show_name()
arthur.show_name()
