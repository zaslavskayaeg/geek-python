def salary_func(hourly_rate, man_hours, bonus):
    '''
    Функция расчета заработной платы сотрудника. В расчете использована формула: (выработка в часах*ставка в час) + премия.
    :param hourly_rate: ставка в час
    :param man_hours: выработка в часах
    :param bonus: премия
    :return: заработная плата до вычета налогов
    '''
    try:
        return (man_hours * hourly_rate) + bonus
    except TypeError:
        return
