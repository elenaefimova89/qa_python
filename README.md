Спринт 4.
Всего проведено 9 тестов.
Тест 1. Проверка, что книга добавляется в коллекцию. test_add_new_book_add_books
Тест 2. Проверка, что устанавливается жанр книги, если книга есть в books_genre и её жанр входит в список genre. test_set_book_genre_works
Тест 3. Проверка, что при вводе названия книги появляется ее жанр. test_get_book_genre_find_book
Тест 4. Проверка, что при вводе жанра выводится список книг с этим жанром. test_get_books_with_specific_genre
Тест 5. Проверка, что возвращается корректный текущий словарь. test_get_books_genre_correct_book_genre
Тест 6. Проверка, что выводятся книги для детей. test_get_books_for_children_genre_age_rating
Тест 7. Проверка, что книга добавляется в избранное 1 раз. test_add_book_in_favorites_one_time
Тест 8. Проверка, что книга удаляется из избранного. test_delete_book_from_favorites_removes
Тест 9. Проверка, что выводится корректный список избранных книг. test_add_book_in_favorites_correct_list
Итого: 9 тестов.

platform win32 -- Python 3.13.3, pytest-8.3.5, pluggy-1.6.0 -- C:\Users\User\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\cygwin64\home\User\qa_python
plugins: cov-6.1.1
collected 17 items

tests.py::TestBooksCollector::test_add_new_book_add_books PASSED         [  5%]
tests.py::TestBooksCollector::test_set_book_genre_works[\u0413\u0430\u0440\u0440\u0438-\u0424\u0430\u043d\u0442\u0430\u0441\u0442\u0438\u043a\u0430] PASSED [ 11%]
tests.py::TestBooksCollector::test_set_book_genre_works[\u041a\u0440\u0438\u043a-\u0423\u0436\u0430\u0441\u044b] PASSED [ 17%]
tests.py::TestBooksCollector::test_set_book_genre_works[\u041c\u0430\u0448\u0430-\u041c\u0443\u043b\u044c\u0442\u0444\u0438\u043b\u044c\u043c\u044b] PASSED [ 23%]
tests.py::TestBooksCollector::test_get_book_genre_find_book[\u0413\u0430\u0440\u0440\u0438-\u0424\u0430\u043d\u0442\u0430\u0441\u0442\u0438\u043a\u0430] PASSED [ 29%]
tests.py::TestBooksCollector::test_get_book_genre_find_book[\u041a\u0440\u0438\u043a-\u0423\u0436\u0430\u0441\u044b] PASSED [ 35%]
tests.py::TestBooksCollector::test_get_book_genre_find_book[\u041c\u0430\u0448\u0430-\u041c\u0443\u043b\u044c\u0442\u0444\u0438\u043b\u044c\u043c\u044b] PASSED [ 41%]
tests.py::TestBooksCollector::test_get_books_with_specific_genre[\u0413\u0430\u0440\u0440\u0438-\u0424\u0430\u043d\u0442\u0430\u0441\u0442\u0438\u043a\u0430] PASSED [ 47%]
tests.py::TestBooksCollector::test_get_books_with_specific_genre[\u041a\u0440\u0438\u043a-\u0423\u0436\u0430\u0441\u044b] PASSED [ 52%]
tests.py::TestBooksCollector::test_get_books_with_specific_genre[\u041c\u0430\u0448\u0430-\u041c\u0443\u043b\u044c\u0442\u0444\u0438\u043b\u044c\u043c\u044b] PASSED [ 58%]
tests.py::TestBooksCollector::test_get_books_genre_correct_book_genre[\u0413\u0430\u0440\u0440\u0438-\u0424\u0430\u043d\u0442\u0430\u0441\u0442\u0438\u043a\u0430] PASSED [ 64%]
tests.py::TestBooksCollector::test_get_books_genre_correct_book_genre[\u041a\u0440\u0438\u043a-\u0423\u0436\u0430\u0441\u044b] PASSED [ 70%]
tests.py::TestBooksCollector::test_get_books_genre_correct_book_genre[\u041c\u0430\u0448\u0430-\u041c\u0443\u043b\u044c\u0442\u0444\u0438\u043b\u044c\u043c\u044b] PASSED [ 76%]
tests.py::TestBooksCollector::test_get_books_for_children_genre_age_rating PASSED [ 82%]
tests.py::TestBooksCollector::test_add_book_in_favorites_one_time PASSED [ 88%]
tests.py::TestBooksCollector::test_delete_book_from_favorites_removes PASSED [ 94%]
tests.py::TestBooksCollector::test_add_book_in_favorites_correct_list PASSED [100%]

============================= 17 passed in 0.05s ==============================
