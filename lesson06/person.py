class Human:
    age: int
    first_name: str
    last_name: str
    weight: int
    _password: str
    __bank_account: str

    counter: int = 0

    def __init__(self, first_name, last_name, age, weight=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.weight = weight
        self.__bank_account = "10000005"
        self._init_password()

        Human.counter += 1

    def info(self):
        print(f"I'm {self.first_name}, age: {self.age}, weight: {self.weight}")

    def _init_password(self):
        self._password = "10293084759837"

    def show_bank_account(self):
        print(f"Account: {self.__bank_account[:5]}*********")

john = Human("John", "Doe", 30)
artur = Human("Artur", "Doe", 40)

print(john, artur)

john.info()
artur.info()

# print(john._password)
# john._init_password()

print(john.counter)
print(artur.counter)
print(Human.counter)

# print(john._Human__bank_account)
john.show_bank_account()


# john.age = 30
# john.first_name = "John"
# john.last_name = "Doe"
#
# artur.age = 40
# artur.first_name = "Artur"
# artur.last_name = "Doe"

# person_dict = {"age": 0, "first_name": "", "last_name": ""}

# print(john.first_name, john.last_name, john.age, john.weight)
# print(artur.first_name, artur.last_name, artur.age, artur.weight)

# john.info()
# Human.info(john)
