from functools import reduce

users_balance = {"john": 340, "artur": 100, "kate": 670}


def my_balance_func(total, amount):
    return total + amount


# users_total = reduce(my_balance_func, users_balance.values())
# sum(users_balance.values())
users_total = reduce(
    lambda total, amount: total + amount,
    users_balance.values()
)

print(users_total)
