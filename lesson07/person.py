class Person:
    def __init__(self, atters: dict):
        self._attributes = atters

    def __del__(self):
        print("Person removed")

    def __str__(self):
        return f"Person {self._attributes['first_name']} {self._attributes['last_name']}"

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, item):
        if item != 'age':
            return self._attributes[item]
        else:
            return None

    def __setattr__(self, key, value):
        if '_attributes' in self.__dict__:
            self._attributes[key] = value
        else:
            super().__setattr__(key, value)


john = Person({'first_name': 'John', 'last_name': 'Doe', 'age': 30})
artur = Person({'first_name': 'Artur', 'last_name': 'Doe', 'age': 40})

# del john

print(john._attributes['first_name'])
print(john)

users = [john, artur]

print(users)

print(john['first_name'])
print(john['age'])

john.job = 'Developer'
print(john['job'])
