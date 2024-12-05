import json
from json import JSONDecodeError


def load_json_data(file_path: str) -> dict:
    """
    Чтение json файла и возвращение данных в виде словаря
    :param file_path: путь к файлу
    """

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except JSONDecodeError:
        return {}


def writing_data_to_json(data: dict, file_path: str):
    """
    Запись данных типа dict в файл json
    :param file_path: путь к файлу
    :param data: словарь с данными для записи в файл
    """

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
