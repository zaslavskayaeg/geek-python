# named_lambda = lambda name: f"Hello, {name}!!!"
#
# print(named_lambda("John"))


print(
    (lambda name: f"Hello, {name}!!!")
    ("John")
)

print(
    (lambda x: x ** 2)
    (2)
)

print(
    (lambda *numbers: numbers)
    (1, 2, 3)
)
