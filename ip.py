import json
import os

class Book:
    def __init__(self, book_id, title, author, year, status, sector, shelf):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        self.sector = sector  # Добавлено поле для сектора
        self.shelf = shelf    # Добавлено поле для полки

class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            with open('books.json', 'r') as f:
                self.books = json.load(f)
        except FileNotFoundError:
            self.books = []

    def save_books(self):
        with open('books.json', 'w') as f:
            json.dump(self.books, f)

    def add_book(self, title, author, year, sector, shelf):
        book_id = len(self.books) + 1
        new_book = Book(book_id, title, author, year, "в наличии", sector, shelf)
        self.books.append(new_book.__dict__)
        self.save_books()

    def search_book(self, search_term):
        found_books = [book for book in self.books if search_term.lower() in book['title'].lower()]
        if found_books:
            for book in found_books:
                print(f"Найдена книга '{book['title']}' в секторе №{book['sector']} на полке {book['shelf']}")
        else:
            print("Книга не найдена.")

    # Остальные методы (удаление, отображение, изменение статуса) остаются без изменений

# Пример использования
library = Library()
library.add_book("Война и мир", "Лев Толстой", 1869, 4, 7)
library.search_book("Война и мир")


def main():
    library = Library()
    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите опцию: ")
        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")
            sector = input("Введите сектор: ")
            shelf = input("Введите полку: ")
            library.add_book(title, author, year, sector, shelf)
        elif choice == '2':
            id = int(input("Введите ID книги для удаления: "))
            library.remove_book(id)
        elif choice == '3':
            query = input("Введите название книги для поиска: ")
            library.search_book(query)
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            id = int(input("Введите ID книги для изменения статуса: "))
            new_status = input("Введите новый статус ('в наличии' или 'выдана'): ")
            library.change_status(id, new_status)
        elif choice == '6':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
