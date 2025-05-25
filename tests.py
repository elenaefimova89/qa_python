import pytest

from main import BooksCollector

class TestBooksCollector:
    # 1. проверяем, что книга добавляется в коллекцию
    def test_add_new_book_add_books(self):
        collector = BooksCollector()
        collector.add_new_book("Крик")
        assert "Крик" in collector.get_books_genre()


    # 2. проверяем, что устанавливает жанр книги, если книга есть в books_genre и её жанр входит в список genre.
    @pytest.mark.parametrize('book,genre', [
        ("Гарри", "Фантастика"),
        ("Крик", "Ужасы"),
        ("Маша", "Мультфильмы")
    ])
    def test_set_book_genre_works(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == genre

    # 3. проверяем, что при вводе названия книги появляется ее жанр
    @pytest.mark.parametrize('book,genre', [
        ("Гарри", "Фантастика"),
        ("Крик", "Ужасы"),
        ("Маша", "Мультфильмы")
    ])
    def test_get_book_genre_find_book(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == genre

    # 4. проверяем, что при вводе жанра выводится список книг с этим жанром
    @pytest.mark.parametrize('book,genre', [
        ("Гарри", "Фантастика"),
        ("Крик", "Ужасы"),
        ("Маша", "Мультфильмы")
    ])
    def test_get_books_with_specific_genre(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_books_with_specific_genre(genre) == [book]

    # 5. проверяем, что возвращается корректный текущий словарь
    @pytest.mark.parametrize('book,genre', [
        ("Гарри", "Фантастика"),
        ("Крик", "Ужасы"),
        ("Маша", "Мультфильмы")
    ])
    def test_get_books_genre_correct_book_genre(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_books_genre() == {book: genre}

    # 6. проверяем, что выводятся книги для детей
    def test_get_books_for_children_genre_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book("Крик")
        collector.set_book_genre("Крик", "Ужасы")
        collector.add_new_book("Маша")
        collector.set_book_genre("Маша", "Мультфильмы")
        assert collector.get_books_for_children() == ["Маша"]

    # 7. проверяем, что книга добавляется в избранное 1 раз
    def test_add_book_in_favorites_one_time(self):
        collector = BooksCollector()
        collector.add_new_book("Крик")
        collector.add_book_in_favorites("Крик")
        collector.add_book_in_favorites("Крик")
        collector.add_book_in_favorites("Крик")
        assert collector.get_list_of_favorites_books() == ["Крик"]

    # 8. проверяем, что книга удаляется из избранного
    def test_delete_book_from_favorites_removes(self):
        collector = BooksCollector()
        collector.add_new_book("Крик")
        collector.add_book_in_favorites("Крик")
        collector.delete_book_from_favorites("Крик")
        assert "Крик" not in collector.get_list_of_favorites_books()

    # 9. проверяем, что выводится корректный список избранных книг
    def test_add_book_in_favorites_correct_list(self):
        collector = BooksCollector()
        collector.add_new_book("Крик")
        collector.add_new_book("Мульт")
        collector.add_new_book("Холмс")
        collector.add_book_in_favorites("Крик")
        collector.add_book_in_favorites("Мульт")
        collector.add_book_in_favorites("Холмс")
        assert collector.get_list_of_favorites_books() == ["Крик", "Мульт", "Холмс"]
