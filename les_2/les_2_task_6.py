# GeekBrains Courses. Python Essential
# Vasilii Sitdikov
# Lesson 2 task 6
# October 2019

# task: 6)	Реализовать структуру данных «Товары» . Она должна представлять собой список кортежей.
        # Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
        # элемента — номер товара и словарь с параметрами (характеристиками товара: название,
        # цена, количество, единица измерения). Структуру нужно сформировать программно, т.е.
        # запрашивать все данные у пользователя.
        # Пример готовой структуры:
        # [
        # (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
        # (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
        # (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
        # ]
        # Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
        # характеристика товара, например название, а значение — список значений-характеристик,
        # например список названий товаров.
        # Пример:
        # {
        # “название”: [“компьютер”, “принтер”, “сканер”],
        # “цена”: [20000, 6000, 2000],
        # “количество”: [5, 2, 7],
        # “ед”: [“шт.”]
        # }
# Solution:
goods = []
features = {'название' : '', 'цена' : '', 'количество' : '', 'единица измерения' : ''}
analytics = {'название' : [], 'цена' : [], 'количество' : [], 'единица измерения' : []}
num = 0
while True:
    if input('Для выхода из программы нажмите "Q", для продолжения "Enter": ').upper() == 'Q':
        break
    num += 1
    for f in features.keys():
        _ = input(f'Введите значение свойства "{f}": ')  # Ввод свойства
        features[f] = int(_) if(f == 'цена' or f == 'количество') else _  # Меняем тип числовых свойства
        analytics[f].append(features[f])  # Добавляем свойство в аналитику
    goods.append((num, features))  # Добавляем свойство в список товаров
    print(f'\n Текущая аналитика по товарам: \n {"*"*30}')
    for key, value in analytics.items():
        print(f'{key[:25]:>30}: {value}')
    print("*"*30)
