"""
Базовые assert

Задание 1

Тест проверяет, что из базы данных пришли данные,
а не их отсутствие None. Допиши проверку


Решение

def test_get_data_from_db_true():
    data = get_data_from_db()  # сохранили данные из БД в переменную

    # пиши код здесь
    assert data != None

Задание 2

Тест подсчитывает, сколько строк из базы данных сохраняются в списке.
В качестве аргумента метод принимает количество значений, которые нужно достать.
Допиши тест, который будет проверять: количество извлеченных записей равно аргументу.

Решение

def test_quantity_of_data_from_db_true():

    quantity = 5
    data = get_data_from_db(quantity)  # сохранили данные из БД в переменную

    # допиши код здесь
    assert len(data) == quantity

Как покрыть тестами метод

Задание 1

Метод get_max_number_from_list возвращает наибольшее число из массива чисел.
В методе есть проверки:
является ли передаваемый в метод аргументом списком;
не пустой ли список;
содержатся ли в списке элементы с типом данных отличных от целого и вещественного чисел.

def get_max_number_from_list(arg):  #объявление метода с соответствующим названием

    if type(arg) is not list:       #проверка на тип аргумента
        return 'Not list!'

    elif arg == []:                 #проверка, не пустой ли список
        return 'List is empty!'

    else:                          #если аргумент является непустым списком
        max_number = arg[0]        #объявление переменной наибольшего числа и присваивание ей в качестве значения по умолчанию первого элемента списка
        for i in arg:              #перебор списка циклом
            if type(i) == int or type(i) == float:   #проверка, что тип элемента в списке - целое число или вещесвтенное
                if i > max_number:        #если элемент из списка больше установленного в переменной
                    max_number = i        #то присвоить новое наибольшее число как значение в переменную max_number
            else:
                return 'List contains a not number type element!' #если проверка на корректный тип элемента (целое или вещественное число) не пройдена, то вернуть соответствующее сообщение
        return max_number          #возвращение наибольшего числа из метода



Допиши код тестов, которые покрывают этот метод.
Первый тест — позитивный: проверяет корректность выполнения метода на правильных входных данных.

Решение

def test_get_max_number_from_list_correct_list():

    arg = [0, 1, 2, 3, 4, -5, 6.5]
    # допиши код здесь
    assert get_max_number_from_list(arg) == 6.5

Задание 2

Второй тест должен проверять, что тип аргумента корректный.
Используй ==.

Решение

def test_get_max_number_from_list_not_list_error():
    arg = 'String'
    # пиши код здесь
    assert get_max_number_from_list(arg) == 'Not list!'

Задание 3

Третий тест должен проверять корректность выполнения условия пустого списка.

Решение

def test_get_max_number_from_list_empty_list_error():
    # пиши код здесь
    empty_list = []
    assert get_max_number_from_list(empty_list) == 'List is empty!'

Задание 4

Четвёртый тест должен проверять, что в списке только целый и вещественный типы.

Решение

def test_get_max_number_from_list_incorrect_type_element_error():
    arg = [1,2,3]
    # пиши код здесь
    assert get_max_number_from_list(arg) == 'List contains a not number type element!'

Как покрыть тестами класс

Задание 1
Есть класс, который управляет коллекцией фильмов. Внутри него:
конструктор, который добавляет фильм в коллекцию;
методы, которые получают фильмы из коллекции по разным параметрам.

class MovieCollection:

    def __init__(self):      #конструктор, который инициализирует пустую коллекцию фильмов
        self.movies = []     #коллекцией будет список: внутри себя словари

    def add_movie(self, name, year, rating):   #метод добавляет фильм в коллекцию. Создает в списке новый объект с ключами: имя, год, рейтинг

        self.movies.append({"name": name,     #добавляет созданный объект в список фильмов
                            "year": year,
                            "rating": rating})

    def get_movies_by_year(self, year):  #метод получения фильмов из коллеции по определенному году

        def filter_func(obj):            #функция сравнения фильмов по году (нужна для функции фильтрации)
            return obj['year'] == year

        movies_by_year = list(filter(filter_func, self.movies)) #функция filter перебирает список фильмов, применяя к каждому объекту функцию сравнения
                #в качестве аргументов встроенная в Python функция "filter" принимает фукнцию сравнения и список, который нужно отфильтровать
        return movies_by_year    #возвращение списка фильмов, которые соответствуют переданному в метод аргументу "year"

    def get_movies_by_more_than_rating(self, rating):  #метод получения фильмов из коллеции выше определенного рейтинга

        def filter_func(object):            #функция сравнения фильмов по рейтингу(нужна для функции фильтрации)
            return object['rating'] >= rating  #рейтинг должен быть выше или равен, чем переданный в аргументе методу

        movies_more_than_rating = list(filter(filter_func, self.movies))

        return movies_more_than_rating  #возвращение списка фильмов, рейтинг которых выше чем переданный в метод аргумент "rating"

    def get_top_of_n_movies(self, n):  #метод получения топ (N) фильмов из коллекции

        def sort_func(movie):        #функция для функции сортировки
            return movie['rating']

        sorted_list = sorted(self.movies, key=sort_func)  #функция сортировки сортирует список по ключу
                #в качестве которого передается функция, возвращающая значение, по которому нужно отсортировать список - рейтинг фильмов
        return sorted_list[-n:]  #возвращение из отсортированного по возрастанию списка последние N фильмов

Решение

    def test_get_movies_by_year_true(self):
    movie_collection = MovieCollection()
    movie_collection.add_movie('The Green Mile', 1999, 9.1)
    movie_collection.add_movie('The Shawshank Redemption', 1994, 9.17)
    movies_by_year.get_movies_by_year('1994')
    assert movies_by_year[0]['year'] == 1994 and len(movies_by_year) == 1

Задание 2

Допиши тест, который проверяет метод get_movies_by_more_than_rating.
Возьми фильмы:
The Green Mile, 1999, 9.1
1+1, 2011, 8.8
Нужно проверить, что из них метод отберёт фильм с рейтингом выше 9.

Решение

def test_get_movies_by_more_than_true(self):
    movie_collection = MovieCollection()
    movie_collection.add_movie('The Green Mile', 1999, 9.1)
    movie_collection.add_movie('1+1', 2011, 8.8)
    movies_more_than_rating.get_movies_by_more_than_rating(9)
    assert movies_by_rating[0]['rating'] > 9

Задание 3

Допиши код, который тестирует метод get_top_of_n_movies.
Проверь эти фильмы:
The Green Mile, 1999, 9.1
1+1, 2011, 8.8
Flight Club, 1999, 8.6

def test_get_top_of_n_movies_true(self):
    movie_collection = MovieCollection()
    movie_collection.add_movie('The Green Mile', 1999, 9.1)
    movie_collection.add_movie('1+1', 2011, 8.8)
    movie_collection.add_movie('Flight Club', 1999, 8.6)
    sorted_list.get_top_of_n_movies(2)
    [movie['rating'] for movie in top_2_movies]
    assert 8.8 in top_2_movies_ratings and 9.1 in top_2_movies_ratings

Как написать параметризованный тест

Задание 2

Параметризуй тест test_email_domain.
Он проверяет, что email оканчивается на @gmail.com.
Функция check_mail уже реализована.
Она принимает на вход email и возвращает True или False в зависимости от проверки.
Список тестовых адресов такой:
['lil_billy_89@gmail.com', 'anna_darmas@gmail.com', 'dragon_slayer666@gmail.com'].
Используй его в декораторе.

Решение

import pytest

def check_mail(mail):
    # строка с email оканчивается на @gmail.com
    return mail.endswith('@gmail.com')


# допиши код, который параметризует тест
@pytest.mark.parametrize ('mail', ['lil_billy_89@gmail.com', 'anna_darmas@gmail.com', 'dragon_slayer666@gmail.com'])
def test_email_domain(mail):
    assert check_mail(mail)


Фикстуры

Задание 1

Класс Mail содержит конструктор с двумя параметрами — sender и receiver, «отправитель» и «получатель»:

class Mail:

    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver

Создай фикстуру mail: она будет возвращать объект класса Mail.
Представь, что класс Mail уже импортирован: писать строчку import Mail не нужно.
Поле sender инициализируй значением 'holmes@yandex.ru', а receiver — значением 'watson@yandex.ru'.

Решение

import pytest

# напиши фикстуру mail
@pytest.fixture

def mail():
    mail = Mail(sender='holmes@yandex.ru', receiver='watson@yandex.ru')
    return mail

Задание 2

Представь, что ты проверяешь работу корзины на сайте:
добавляешь несколько товаров в корзину,
получаешь список продуктов, которые лежат в корзине,
сохраняешь список в переменную cart.
cart = ['апельсиновый сок', 'манго', 'молоко']
Помести переменную cart в фикстуруproduct_list.
Напиши тест  test_cart_item_in_product_list: он должен проверить, что товар манго есть в списке продуктов, которые лежат в корзине.


Решение

import pytest


@pytest.fixture
def product_list():
    cart = ['апельсиновый сок', 'манго', 'молоко']
    return cart


def test_cart_item_in_product_list(product_list):
    assert 'манго' in product_list


Особенности фикстур

Задание
Напиши фикстуру products, которая возвращает список ['apple'].
Затем создай ещё одну  фикстуру append_product, которая добавит элемент 'orange' в этот список.
Выполни тест test_product_list_two_items_is_in_received_list, который будет использовать эти две фикстуры.
Проверь с помощью цикла, что элементы apple и orange есть в полученном списке.


Решение


import pytest
# напиши фикстуру products
@pytest.fixture
def products():
    products=['apple']
    return products
# напиши фикстуру append_product
@pytest.fixture
def append_product(products):
    append_product = products.append('orange')
    return products
# напиши тест test_product_list
def test_product_list_two_items_is_in_received_list(products, append_product):
    for i in 'orange', 'apple':
        assert i in products


Параметры scope и autouse


Задание 1

Напиши фикстуру city_name, которая возвращает пустой список [].
Затем создай ещё одну фикстуру append_city, которая добавит город Москва в этот список. Для обоих фикстур используй параметрscope="session".
После этого добавь тест test_city_name_one_city_is_in_received_list в состав класса TestClassCityName.
Тест должен проверять, что получается список ['Москва'].
Используй обе фикстуры.
Создай второй класс TestClassCityNameWithoutAppend.
В его составе создай тест  test_city_name_one_city_is_in_received_list.
Он должен использовать только фикстуру city_name. Проверить, что получается список ['Москва'].

Решение

import pytest

# напиши фикстуру city_name
@pytest.fixture(scope="session")
def city_name():
    city_name = []
    return city_name
# напиши фикстуру append_city
@pytest.fixture(scope="session")
def append_city(city_name):
    append_city = city_name.append('Москва')
    return append_city

class TestClassCityName:
    def test_city_name_one_city_is_in_received_list(self, city_name, append_city):
        assert 'Москва' in city_name

class TestClassCityNameWithoutAppend():
    def test_city_name_one_city_is_in_received_list(self, city_name):
        assert 'Москва' in city_name

Задание 2

В составе класса TestWeather напиши фикстуру weather. Она возвращает текст Температура воздуха составляет 25 градусов тепла.
Установи значение autouse=True.Добавь тест test_weather_return_text.
Он должен проверить, что weatherсодержит текст Температура воздуха составляет 25 градусов тепла.
Добавь ещё один тест test_weather_change_return_new_text.
Он поменяет температуру с 25 на 10 градусов.
И проверит, что получился новый текст Температура воздуха составляет 10 градусов тепла.
Оба теста должны использовать фикстуру автоматически.


Решение

import pytest
class TestWeather:
    @pytest.fixture(autouse=True)
    def weather(self):
        self.weather='Температура воздуха составляет 25 градусов тепла'
        return self.weather

# напиши тест test_weather_return_text
    def test_weather_return_text(self):
        assert self.weather=='Температура воздуха составляет 25 градусов тепла'
# напиши тест test_weather_change_return_new_text

    def test_weather_change_return_new_text(self):
        self.weather=self.weather.replace('25','10')
        assert self.weather=='Температура воздуха составляет 10 градусов тепла'

"""

"""

                                                        ФИНАЛЬНЫЙ ПРОЕКТ 2 СПРИНТА
                                                        
Переходи по данной ссылке на Github - решение в ветке Develop
https://github.com/denisofflive/qa_python/tree/develop

"""




