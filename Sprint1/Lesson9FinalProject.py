"""Задание 1

Строка содержит пять временных значений. Они записаны через запятую:

'1h 45m,360s,25m,30m 120s,2h 60s'.

Напиши цикл, который посчитает общее количество минут.
Результат сохрани в переменную и выведи на экран.
Используй в решении методы split(), replace() и оператор in.
Обрати внимание: временное значение может состоять из одного, двух или трёх единиц времени.

Значения расшифровываются так:
часы — любое положительное целое число и символ h;
минуты — любое положительное целое число и символ m;
секунды — положительное целое число кратное 60 и символ s."""

# РЕШЕНИЕ 1

a = '1h 45m,360s,25m,30m 120s,2h 60s'
a_without_space = a.replace(' ', ",")
a_list = a_without_space.split(',')
summ_time = 0
for i in a_list:
    if "h" in i:
        time = int(i.split('h')[0])
        summ_time += time * 60
    elif "m" in i:
        time_m = int(i.split('m')[0])
        summ_time += time_m
    else:
        time = int(i.split('s')[0])
        summ_time += time / 60
print(int(summ_time))


"""

Задание 2


Исправь класс Tester так, чтобы:

при вызове метода work_hard у экземпляра класса tester_1 печаталось 'tester_1 Можно отдыхать';
при вызове метода work_hard у экземпляра класса tester_2 печаталось 'tester_2 Что ж, ещё часок поработаю!'.

Вызовы менять не нужно!!!

КОД

class Tester:

    def __init__(name):
        name = name
        deadline = True

    def work_hard(self, deadline=True):
        if self.deadline:
            print(self.name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.name, 'Можно отдыхать')

tester_1 = Tester(name='tester_1')
tester_1.work_hard(deadline=False)  # 'tester_1 Можно отдыхать'
tester_2 = Tester(name='tester_2')
tester_2.work_hard(deadline=True)   # 'tester_2 Что ж, ещё часок поработаю!'

"""

# РЕШЕНИЕ 2

class Tester:

    def __init__(self, name):
        self.name = name

    def work_hard(self, deadline=True):
        if deadline:
            print(self.name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.name, 'Можно отдыхать')

tester_1 = Tester(name ='tester_1')
tester_1.work_hard(deadline=False)  # 'tester_1 Можно отдыхать'
tester_2 = Tester(name='tester_2')
tester_2.work_hard(deadline=True)   # 'tester_2 Что ж, ещё часок поработаю!'

"""

Задание 3


Словарь содержит информацию о чемпионатах по футболу в 21 веке:
год. Например, 1988;
страна, которая выиграла чемпионат мира по футболу. Например, Англия.

Что нужно сделать:

Добавь в словарь 2022 год. В 2022 году чемпионом стала Аргентина.
Выведи на экран всех чемпионов в формате год - страна.
Проверь, выигрывала ли Италия в 21 веке.
Есть переменная countryсо значением Италия.
Проверь, содержится ли она в словаре.
Если да, выведи надпись Италия cтановилась чемпионом мира по футболу в 21 веке!
А если страна отсутствует среди значений словаря, выведи на экран Италия не выигрывала чемпионат мира по футболу в 21 веке.


КОД

world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

...

country = 'Италия'

... 

"""

# РЕШЕНИЕ 3

world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions[2022] = "Аргентина"

countryco = 'Италия'

world_champions[2022] = 'Аргентина'

# Выводим список всех чемпионов
for year, country in world_champions.items():
    print(f"{year} - {country}")

# Проверяем, выигрывала ли Италия в 21 веке
if countryco in world_champions.values():
    print("Италия становилась чемпионом мира по футболу в 21 веке!")
else:
    print("Италия не выигрывала чемпионат мира по футболу в 21 веке.")


"""

Задание 4



Есть два списка задач. Список new_tasks содержит задачи, которые по плану нужно протестировать до конца месяца.
Список completed_tasks — уже завершенные в текущем месяце.

Что нужно сделать:

Тестировщик только что завершил задачу task_005.
Перенеси её из списка new_tasks в список completed_tasks. Сделай это в одно действие.
Запрос task_007 заказчик убрал из плана, потому что нужно доработать требования.
Удали его из списка new_tasks.
Последней задаче из списка new_tasks заказчик поднял приоритет, поэтому её нужно будет взять в работу следующей.
Выведи её на экран.

КОД

new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

"""

# РЕШЕНИЕ 4

new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

# Перенос задачи
completed_tasks.append(new_tasks.pop(4))

# Удаление задачи
new_tasks.remove('task_007')

print(new_tasks[-1])


"""

Задание 5


Напиши класс TestCase. Он должен содержать конструктор и методы.
В конструкторе инициализируются поля:
steps — шаги тест-кейса, в качестве параметра принимает пустой словарь;
result — ожидаемый результат выполнения тест-кейса, принимает None в качестве параметра.

Методы:

Метод set_step — добавляет в словарь steps шаг тест-кейса.
Принимает два параметра: step_number и step_text.
Ключ — это step_number(номер шага), а значение — step_text (текстовое описание шага).
Метод delete_step — удаляет шаг из steps по ключу step_number, который передали в метод.
Метод set_result — устанавливает ожидаемый результат. Он помещает его в атрибут result по параметру result, который передали методу.
Метод get_test_case — печатает информацию о составе тест-кейса в формате {'Шаги': {<номер шага>: '<описание шага>'}, 'Ожидаемый результат': '<вывод ожидаемого результата>'}.

Пример вывода метода get_test_case:

{
    'id': 988, 
    'Название': 'Добавление товара в корзину', 
    'Шаги': {
            1: 'Перейти на сайт', 
            2: 'Перейти в раздел Товары', 
            3: 'Нажать кнопку «В корзину» у первого товара'
    }, 
    'Ожидаемый результат': 'Товар окажется в корзине'
} 


КОД


class TestCase:

    def __init__(self):
   ...
   ...

test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case()

"""

# РЕШЕНИЕ 5

class TestCase:
    def __init__(self):
        self.steps = {}
        self.result = None

    def set_step(self, step_number, step_text):
        self.steps[step_number] = step_text

    def delete_step(self, step_number):
        del self.steps[step_number]

    def set_result(self, result):
        self.result = result

    def get_test_case(self):
        return {
            'Шаги': self.steps,
            'Ожидаемый результат': self.result
        }

test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()


test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case()

print(test_case_1.get_test_case())
print(test_case_2.get_test_case())

