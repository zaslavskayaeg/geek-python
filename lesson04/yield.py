def user_generator():
    for user in ("Jhon", "Kate", "Artur"):
        yield user


# print(user_generator())

for user_item in user_generator():
    print(user_item)
