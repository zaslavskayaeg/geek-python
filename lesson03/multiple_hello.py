users = ["John", "Arthur", "Kate", "Jane"]


def say_hello(*user_list, **user_settings):
    for user in user_list:
        print(user)


say_hello(*users)
