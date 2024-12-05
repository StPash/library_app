import datetime


def is_alph_num_and_space(line: str):
    """
    Проверка: строка состоит из букв, цифр и пробелов
    :param line: строка текста
    """

    line = line.replace(' ', 'a')
    return line.isalnum()


def is_alph_and_space(line: str):
    """
    Проверка: строка состоит из букв и пробелов
    :param line: строка текста
    """

    line = line.replace(' ', 'a')
    return line.isalpha()


def is_correct_year(line: str):
    """
    Проверка: введённая строка - это год (4-х значное число) не больше текущего года
    :param line:  строка текста
    """

    if line.isdigit() and len(line) == 4:
        year = int(line)
        if year <= datetime.datetime.now().year:
            return True
        else:
            return False
    else:
        return False


def is_book_status(line: str):
    """
    Проверка: в ведённой строке указан один из вариантов статуса книги
    :param line: строка текста
    """

    if line.lower() in ('в наличии', 'выдана'):
        return True
    else:
        return False
