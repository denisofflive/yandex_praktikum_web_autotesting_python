"""

СЛОВАРИ И КОЛЛЕКЦИИ.

Как получить и изменить значение в словаре

Задание 1

В словаре neighbours хранятся номера квартир и имена жильцов.
Допиши код, чтобы на экран выводилось имя жильца квартиры 26.

"""

neighbours =  {
    11 : 'Александр',
    21 : 'Василий',
    26 : 'Антон',
    9 : 'Евгений'
}
# твой код здесь
print(neighbours[26])

"""

Задание 2

Потренируйся менять значения в словаре. 
В 21-й квартире теперь живёт не Василий, а Лиза.
Замени значение на новое по ключу.

"""

neighbours =  {
    11 : 'Александр',
    21 : 'Василий',
    26 : 'Антон',
    9 : 'Евгений'
}
# твой код здесь
neighbours[21] = 'Лиза'

print('Теперь в квартире 21 живёт', neighbours[21])

"""

Как добавить элементы в словарь

Задание 1
Добавь в словарь neighbours ещё две пары ключ — значение: 
Допиши в объявление словаря новые ключи и значения: пусть в квартире 2 живёт Толик, а в 7 — Гена.
Выведи на экран словарь neighbours.

"""

neighbours =  {
    11 : 'Александр',
    21 : 'Лиза',
    26 : 'Антон',
    9 : 'Евгений',
    5 : 'Катя',
    33 : 'Сергей'
}
new_neighbours = {2: 'Толик', 7: 'Гена'}

neighbours.update(new_neighbours)

print(neighbours)

"""

Задание 2

Добавь в словарь neighbours новый элемент по ключу.
Пусть нового жильца зовут Даниил, а его квартира — 47.
После этого напечатай словарь neighbours.

"""

neighbours =  {
    11 : 'Александр',
    21 : 'Лиза',
    26 : 'Антон',
    9 : 'Евгений',
    5 : 'Катя',
    33 : 'Сергей',
    2 : 'Толик',
    7 : 'Гена'
}

# твой код
neighbours[47] = 'Даниил'

print(neighbours)

"""
Задание 3

Добавь все элементы словаря new_neighbours в словарь neighbours. 
После этого напечатай словарь neighbours, чтобы убедиться, что всё получилось.

"""

neighbours =  {
    11 : 'Александр',
    21 : 'Лиза',
    26 : 'Антон',
    9 : 'Евгений',
    5 : 'Катя',
    33 : 'Сергей',
    2 : 'Толик',
    7 : 'Гена'
}

new_neighbours =  {
    19 : 'Арсений',
    38 : 'Дима',
    3 : 'Никита'
}

# твой код
neighbours.update(new_neighbours)

print(neighbours)

"""
Метод get()

Задание 1

Потренируйся находить значения методом get(): выведи на экран жильцов 11-й и 9-й квартир.

"""

neighbours = {
    11: 'Александр',
    21: 'Василий',
    26: 'Антон',
    9: 'Евгений'
}

# твой код здесь
print(neighbours.get(11))
print(neighbours.get(9))

"""
Задание 2

Напиши метод get() с сообщением об ошибке:
пусть он попробует найти жильца 25-й квартиры,
а если такой нет — выведет на экран «Тут никто не живёт».

"""
neighbours = {
    11: 'Александр',
    21: 'Василий',
    26: 'Антон',
    9: 'Евгений'
}

# твой код здесь
print(neighbours.get(25,'Тут никто не живёт'))

"""

Методы keys() и values()

Задание

Список жильцов обновился: теперь там шесть квартир.
Допиши код, чтобы вывести номера квартир и имена жильцов в таком формате:

11 - Александр
21 - Лиза
26 - Антон
... 

Тебе понадобится перебрать в цикле каждый ключ из коллекции neighbours.keys().

"""
neighbours =  {
    11 : 'Александр',
    21 : 'Лиза',
    26 : 'Антон',
    9 : 'Евгений',
    5 : 'Катя',
    33 : 'Сергей'
}

# твой код здесь
for flat in neighbours.keys():
    print(flat, '-', neighbours[flat])


"""

Перебор элементов в словаре

Задание 1

Попробуй составить словарь neighbours из двух списков. 
В коде приготовлены два списка: 
neighbours_names — имена жильцов;
neighbours_flats — квартиры, где они живут.
Списки соответствуют друг другу: например, жилец neighbours_names[0] живёт в квартире neighbours_flats[0].
Заполни элементами словарь neighbours — он уже объявлен в коде.
Ключом каждого элемента должен быть номер квартиры, значением — имя.
Для этого в цикле создай элементы словаря из элементов списков с одинаковыми индексами.
Для проверки выведи на экран сообщение "<Имя> живёт в квартире <квартира>".
Используй доступ по нужному ключу в словаре neighbours.

"""

neighbours_names = ['Вася', 'Ира', 'Антон', 'Арина', 'Женя']
neighbours_flats = [4, 9, 12, 16, 19]


neighbours = {}


# Допиши код сюда
for i in range(0, len(neighbours_names)):
    neighbours[neighbours_flats[i]] = neighbours_names[i]
    print(neighbours.get(neighbours_flats[i]) + ' живёт в квартире ' + str((neighbours_flats[i])))

"""
Задание 2

Словарь обновился: теперь в каждой квартире по два жильца.
Значения словаря — это списки из двух имён.
Напечатай обо всех жильцах такое сообщение: <имена> живут в квартире <номер_квартиры>.

"""

neighbours =  {
    11 : ['Александр', 'Света'],
    21 : ['Лиза', 'Артём'],
    26 : ['Антон', 'Надя'],
    9 : ['Евгений', 'Маша'],
    5 : ['Катя', 'Костя'],
    33 : ['Сергей', 'Инга']
}

# твой код здесь
for key, value in neighbours.items():
    print(value[0] + ", " + value[1] + " живут в квартире " + str(key))

"""
Задание 3

Выведи на экран:
Сколько людей живёт в квартире 11 — числом.
Всех жильцов квартиры 21.
Имена всех вторых жильцов квартир.
Вывод должен выглядеть примерно так:

2
Александр
Света
Света
Артём
... 

"""

neighbours =  {
    11 : ['Александр', 'Света'],
    21 : ['Лиза', 'Артём'],
    26 : ['Антон', 'Надя'],
    9 : ['Евгений', 'Маша'],
    5 : ['Катя', 'Костя'],
    33 : ['Сергей', 'Инга']
}

# Выведи на экран, сколько людей живёт в квартире 11 (число)
print(len(neighbours[11]))

# Выведи на экран построчно всех жильцов квартиры 21
for name in neighbours[21]:
    print(name)

# Выведи на экран имена всех вторых жильцов
for flat_owners in neighbours.values():
    print(flat_owners[1])

"""
Словари: практика

Задание 1

В доме есть пять свободных квартир с номерами от 1 до 5.
Нужно заселить их жильцами. Списки упорядочены по номерам квартир жильцов.
Создай словарь, где ключ — номер квартиры, а значение — списки с именами жильцов.
Каждая пара жильцов — это отдельный список.

"""

new_neighbours = [['Вася', 'Катя'], ['Юра', 'Марина'], ['Лёша', 'Ира'], ['Петя', 'Надя'], ['Ваня', 'Света']]

house_dict = {}

for i in range(1, len(new_neighbours) + 1):
    house_dict[i] = new_neighbours[i-1]

print(house_dict)

"""
Задание 2


Есть много мнемонических правил, чтобы запомнить цвета радуги.
Одно из них звучит так: каждый охотник желает знать где сидит фазан.
Первая буква в каждом слове обозначает один из цветов радуги:
к — красный;
о — оранжевый;
ж — жёлтый;
з — зелёный;
г — голубой;
с — синий;
ф — фиолетовый.
Есть два списка.
Список со словами из мнемонической фразы. Слова идут по порядку:
первая буква в слове соответствует цвету радуги в порядке, который записан выше.
mnemo = ['каждый', 'охотник', 'желает', 'знать', 'где', 'сидит', 'фазан'] 
Список с цветами радуги. Цвета записаны не по порядку, перемешаны.
colors = [
  'оранжевый', 'голубой', 'фиолетовый', 'красный', 'желтый', 'синий', 'зеленый'
] 
Твоя задача — наполнить словарь rainbow_dict парами ключ-значение.
Ключ — слово из списка mnemo, а значение — соответствующий слову цвет из списка colors.
Выведи словарь. Должно получиться так:
{'каждый': 'красный', 'охотник': 'оранжевый', 'желает': 'желтый', 'знать': 'зеленый', 'где': 'голубой', 'сидит': 'синий', 'фазан': 'фиолетовый'}
"""
mnemo = ['каждый', 'охотник', 'желает', 'знать', 'где', 'сидит', 'фазан']

colors = ['оранжевый', 'голубой', 'фиолетовый', 'красный', 'желтый', 'синий', 'зеленый']

...  # создай словарь rainbow_dict
rainbow_dict = {}

...  # наполни словарь элементами
for key in mnemo:
    for color in colors:
        if color[0] == key[0]:
            rainbow_dict[key] = color

# твой код

print(rainbow_dict)

"""
Задание 3

Словарь movies состоит из пар Название фильма и его Оценка. 
movies = {'Игры разума': 8.3, 'Зеленая миля': 9.1, 'Леон': 8.5, 'Эффект бабочки': 8.2, 'Матрица': 8.6, 'Криминальное чтиво': 8.7} 
Твоя задача — отфильтровать фильмы по оценке.
Оставь только те, у которых она больше или равна 8.5.
Отфильтрованные пары запиши в новый словарь filtered_movies и выведи его на экран.

"""

movies = {'Игры разума': 8.3, 'Зеленая миля': 9.1, 'Леон': 8.5, 'Эффект бабочки': 8.2, 'Матрица': 8.6, 'Криминальное чтиво': 8.7}

filtered_movies = {}

for key, value in movies.items():
    if value >= 8.5:
        filtered_movies[key] = value

print(filtered_movies)