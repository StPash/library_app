import os

from utils.working_with_json import load_json_data, writing_data_to_json


class LibraryManager:
    """
    Класс отвечающий за работы с базой хранения записей о книгах
    """
    _JSON_FILE_NAME = 'library_database.json'

    _BOOK_DATABASE_JSON_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    _BOOK_DATABASE_JSON_FILE_PATH = os.path.join(_BOOK_DATABASE_JSON_DIR, _JSON_FILE_NAME)

    @classmethod
    def add_book(cls, title: str, author: str, year: int):
        """
        Добавление новой записи
        :param title: Название книги
        :param author: Автор в формате Ф И О
        :param year: Год издания
        """

        data = load_json_data(cls._BOOK_DATABASE_JSON_FILE_PATH)
        keys = [int(key) for key in data.keys()]

        new_id = max(keys) + 1 if keys else 1
        new_entry = {str(new_id): {
            "id": new_id,
            "title": title,
            "author": author,
            "year": year,
            "status": "в наличии"
        }}
        data.update(new_entry)

        writing_data_to_json(data, cls._BOOK_DATABASE_JSON_FILE_PATH)
        return new_id

    @classmethod
    def delete_book(cls, book_id: str):
        """
        Удаление записи о книге по id
        :param book_id: id книги
        """

        data = load_json_data(cls._BOOK_DATABASE_JSON_FILE_PATH)
        if book_id in data:
            del data[book_id]
            writing_data_to_json(data, cls._BOOK_DATABASE_JSON_FILE_PATH)
            return True
        else:
            return False

    @classmethod
    def search_book(cls, title: str, author: str, year: int):
        """
        Поиск книг по указанным параметрам
        :param title: Название книги
        :param author: Автор
        :param year: Год издания
        """

        search_fields = {"title": None,
                         "author": None,
                         "year": None}

        if not title:
            del search_fields["title"]
        else:
            search_fields["title"] = title

        if not author:
            del search_fields["author"]
        else:
            search_fields["author"] = author

        if not year:
            del search_fields["year"]
        else:
            search_fields["year"] = year

        if not search_fields:
            return False

        data = load_json_data(cls._BOOK_DATABASE_JSON_FILE_PATH)
        search_result = []

        for book_data in data.values():
            for search_field in search_fields:
                if not book_data[search_field] == search_fields[search_field]:
                    break
            else:
                search_result.append(book_data)

        return search_result

    @classmethod
    def get_book_list(cls):
        """
        Загрузка списка записей из файла хранения
        """

        data = load_json_data(cls._BOOK_DATABASE_JSON_FILE_PATH)
        return data.values()

    @classmethod
    def update_book_status(cls, book_id: str, status: str):
        """
        Обновление статуса книги
        :param book_id: id книги
        :param status: новый статус: в наличии или выдана
        """

        data = load_json_data(cls._BOOK_DATABASE_JSON_FILE_PATH)
        if book_id in data:
            data[book_id]['status'] = status
            writing_data_to_json(data, cls._BOOK_DATABASE_JSON_FILE_PATH)
            return True
        else:
            return False
