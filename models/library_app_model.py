from models.library_manager import LibraryManager
from utils.correct_input import correct_input, correct_input_or_none
from utils.display_dict_list import display_dict_list
from utils.validation import is_alph_num_and_space, is_correct_year, is_alph_and_space, is_book_status


class LibraryApp:
    """
    Класс отвечающий за обработку команд, поступающих в командную строку
    """
    @classmethod
    def call_command(cls, command: str):
        """
        Проверяет корректность (наличие) введённой команды, вызывает соответсвующий метод, при корректном вводе
        :param command: команда введённая пользователем
        """

        commands = {
            'add_book': cls.add_book,
            'delete_book': cls.delete_book,
            'get_book_list': cls.get_book_list,
            'update_book_status': cls.update_book_status,
            'search_book': cls.search_book
        }
        if command in commands:
            commands[command]()
        else:
            print('Команда отсутствует или введена некорректно')

    @classmethod
    def add_book(cls):
        """
        Предоставляет функционал по добавлению книги в базу:
        ввод необходимых данных со стороны пользователя,
        перенаправление этих данных в LibraryManager для создания записи
        """

        message = 'Введите название книги'
        title = correct_input(message, is_alph_num_and_space).upper()

        message = 'Укажите автора книги в следующем формате: Фамилия Имя Отчество(если имеется)'
        author = correct_input(message, is_alph_and_space).title()

        message = 'Введите год издания книги'
        year = int(correct_input(message, is_correct_year))

        new_book_id = LibraryManager.add_book(title, author, year)
        print(f'Книга успешно добавлена (присвоенный id: {new_book_id})')

    @classmethod
    def delete_book(cls):
        """
        Предоставляет функционал по удалению книги из базы:
        ввод необходимых данных со стороны пользователя,
        перенаправление этих данных в LibraryManager для удаления записи
        """

        message = 'Введите id книги, которую хотите удалить'
        book_id = correct_input(message, str.isdigit)

        if LibraryManager.delete_book(book_id):
            print('Книга успешно удалена из базы')
        else:
            print('В базе отсутствует книга с указанным id')

    @classmethod
    def get_book_list(cls):
        """
        Совершает запрос к LibraryManager для получения списка книг и выводит его пользователю
        """

        book_list = LibraryManager.get_book_list()
        if not book_list:
            print('В базе данных ещё нет записей\n')
        display_dict_list(book_list)

    @classmethod
    def update_book_status(cls):
        """
        Предоставляет функционал по обновлению статуса книги:
        ввод необходимых данных со стороны пользователя,
        перенаправление этих данных в LibraryManager для обновления записи
        """

        message = 'Введите id книги, статус которой хотите изменить'
        book_id = correct_input(message, str.isdigit)

        message = f'Укажите статус, который хотите установить для книги с id: {book_id} ("в наличии" или "выдана")'
        status = correct_input(message, is_book_status).lower()

        if LibraryManager.update_book_status(book_id, status):
            print('Статус книги обновлен')
        else:
            print('В базе отсутствует книга с указанным id')

    @classmethod
    def search_book(cls):
        """
        Предоставляет функционал по поиску книги в базе:
        ввод необходимых данных со стороны пользователя,
        перенаправление этих данных в LibraryManager для поиска записей
        """

        print("Поиск книги можно осуществлять по названию, автору и году издания,\n"
              "как отдельно по каждому параметру, так и в комбинации.\n"
              "Вам будет предложено ввести каждый из указанных параметров,\n"
              "если какой-либо из них вам не нужен при поиске, введите пробел и нажмите Enter\n")

        message = 'Введите название книги'
        title = correct_input_or_none(message, is_alph_num_and_space).upper()

        message = 'Укажите автора книги в следующем формате: Фамилия Имя Отчество(если имеется)'
        author = correct_input_or_none(message, is_alph_and_space).title()

        message = 'Введите год издания книги'
        year = correct_input_or_none(message, is_correct_year)
        if year:
            year = int(year)

        search_result = LibraryManager.search_book(title, author, year)
        if not search_result:
            print(f'\nНет результатов оп Вашему запросу: {title} {author} {year}')
        else:
            print(f'\nРезультат оп Вашему запросу: {title} {author} {year}')
            display_dict_list(search_result)
