from models.library_app_model import LibraryApp


def main():
    while True:
        print("""\nВведете следующие команды для выполнения указанных функций:
        add_book - для добавления новой записи в базу данных;
        delete_book - для удаления книги по id;
        get_book_list - для получения списка всех записей в базе данных;
        update_book_status - для обновления статуса книги по id;
        search_book - для поиска книги в базе данных
        exit - для прекращения работы программы\n
        """)
        try:
            command = input()
            if command == 'exit':
                break
            LibraryApp.call_command(command.strip())
        except FileNotFoundError:
            print('Файл "library_database.json" для хранения записей не обнаружен')


if __name__ == "__main__":
    main()
