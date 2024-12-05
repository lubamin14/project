import json
import os


class Book:
    def __init__(self, id, title, author, year, status="в наличии", sector=None, shelf=None):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        self.sector = sector
        self.shelf = shelf

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
            "sector": self.sector,
            "shelf": self.shelf
        }

class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def load_books(self):
        if os.path.exists("library.json"):
            with open("library.json", "r", encoding="utf-8") as f:
                books_data = json.load(f)
                for book_data in books_data: self.books.append(Book(**book_data))

    def save_books(self):
        with open("library.json", "w", encoding="utf-8") as f:
            json.dump([book.to_dict() for book in self.books], f, ensure_ascii=False, indent=4)

    def add_book(self, title, author, year, sector, shelf):
        id = len(self.books) + 1
        book = Book(id, title, author, year, sector=sector, shelf=shelf)
        self.books.append(book)
        self.save_books()
        print(f"Книга '{title}' добавлена с ID {id}.")

    def remove_book(self, id):
        for book in self.books:
            if book.id == id:
                self.books.remove(book)
                self.save_books()
                print(f"Книга с ID {id} удалена.")
                return
        print(f"Книга с ID {id} не найдена.")

    def search_book(self, query):
        found_books = [book for book in self.books if query.lower() in book.title.lower()]
        if found_books:
            for book in found_books:
                print(f"Найдена книга '{book.title}' автор: {book.author}, "
                      f"сектор: {book.sector}, полка: {book.shelf}.")
        else:
            print("Книги не найдены.")

    def display_books(self):
        for book in self.books:
            print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, "
                  f"Год: {book.year}, Статус: {book.status}, "
                  f"Сектор: {book.sector}, Полка: {book.shelf}.")

    def change_status(self, id, new_status):
        for book in self.books:
            if book.id == id:
                book.status = new_status
                self.save_books()
                print(f"Статус книги с ID {id} изменён на '{new_status}'.")
                return
        print(f"Книга с ID {id} не найдена.")


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