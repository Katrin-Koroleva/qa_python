from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    #тест, который проверяет, что нельзя добавить одну и ту же книгуу дважды
    def test_add_new_book_adding_duplicate_book(self):
        collector = BooksCollector()
        collector.add_new_book("1984")
        collector.add_new_book("1984")  # вторая попытка добавить ту же самую книгу
        assert collector.get_books_rating() == {"1984": 1}

    #тест, который проверяет, что нельзя добавить рейтинг для книги, которой нет в списке
    def test_set_book_rating_for_nonexistent_book(self):
        collector = BooksCollector()
        collector.set_book_rating("Nonexistent Book", 5)
        assert collector.get_books_rating() == {}

    #Нельзя выставить рейтинг меньше 1
    def test_set_book_rating_for_rating_below_one(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_rating('1984', -1)
        assert collector.get_book_rating("1984") == 1

    #Нельзя выставить рейтинг больше 10
    def test_set_book_rating_for_rating_over_ten_rating_is_one(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_rating('1984', 11)
        assert collector.get_book_rating('1984') == 1

    #У не добавленной книги нет рейтинга
    def test_get_book_rating_for_nonexisting_book_rating_is_none(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        assert collector.get_book_rating('Harry Potter') is None

    #тест на добавление книги в избранное
    def test_add_book_in_favorites_add_one_book_book_is_added(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        favorites = collector.get_list_of_favorites_books()
        assert favorites[0] == '1984'

    #тест нельзя добавить книгу в избранное, если ее нет в словаре
    def test_add_book_in_favorites_book_not_in_dictionary_favorites_is_empty(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('1984')
        favorites = collector.get_list_of_favorites_books()
        assert favorites == []

    #тест проверка удаления книги из избранного
    def test_delete_book_from_favorites_delete_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('It')
        collector.add_book_in_favorites('1984')
        collector.add_book_in_favorites('It')

        collector.delete_book_from_favorites('It')
        favorites = collector.get_list_of_favorites_books()
        assert 'It' not in favorites

    #тест на получения списка книг с определенным рейтингом
    def test_get_books_with_specific_rating_of_existing_book_with_existing_rating(self):
            collector = BooksCollector()
            collector.add_new_book('1984')
            collector.add_new_book('Animal Farm')
            collector.add_new_book('It')
            collector.set_book_rating('1984', 8)
            collector.set_book_rating('Animal Farm', 7)
            collector.set_book_rating('It', 9)

            rating_8_books = collector.get_books_with_specific_rating(8)
            assert len(rating_8_books) == 1 and '1984' in rating_8_books


    #тест на получение рейтинга книги по ее имени
    def test_get_book_rating_for_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_rating('1984', 9)
        rating = collector.get_book_rating('1984')
        assert rating == 9

    #тест на получения списка избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('It')
        collector.add_book_in_favorites('1984')
        collector.add_book_in_favorites('It')
        favorites = collector.get_list_of_favorites_books()
        assert favorites == ['1984', 'It']

