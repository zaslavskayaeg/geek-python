# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_info(first_name, last_name, birth_year, city, email, phone):
    '''
    Возврат строки с данными о пользователе
    :param first_name: имя
    :param last_name: фамилия
    :param birth_year: год рождения
    :param city: город проживания
    :param email: email
    :param phone: телефон
    :return: Строка с данными о пользователе
    :rtype: str
    '''

    return f'{first_name} {last_name}, {birth_year} года рождения, проживает в городе {city}. e-mail:{email}; тел:{phone}'


print(user_info(first_name='John', last_name='Smith', birth_year=1580, city='Jamestown', email='john@smith.com',
                phone=19999999999))
