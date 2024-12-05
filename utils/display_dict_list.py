def display_dict_list(dict_list: list):
    """
    Вывод данных хранящихся в списке словарей построчно для каждого словаря в формате key: value через запятую
    :param dict_list: список словарей
    :return:
    """
    for dict_el in dict_list:
        for key, value in dict_el.items():
            print(f'{key}: {value}', end=', ')
        print()
