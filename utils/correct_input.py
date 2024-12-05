def correct_input(message: str, valid_func):
    """
    Обеспечивает корректный ввод данных, корректность данных определяется передаваемой функцией
    :param message: сообщение пользователю (об ожидаемом вводе данных)
    :param valid_func: функция для проверки введенных данных
    """

    while True:
        print(message)
        arg = input().strip()
        if valid_func(arg):
            return arg.strip()
        else:
            print('Введённые данные некорректны, попробуйте снова')


def correct_input_or_none(message: str, valid_func):
    """
    Обеспечивает корректный ввод данных, корректность данных определяется передаваемой функцией,
    но также допускает отсутствие данных на входе
    :param message: сообщение пользователю (об ожидаемом вводе данных)
    :param valid_func: функция для проверки введенных данных
    """

    while True:
        print(message)
        arg = input().strip()
        if not arg:
            return ''
        if valid_func(arg):
            return arg.strip()
        else:
            print('Введённые данные некорректны, попробуйте снова')