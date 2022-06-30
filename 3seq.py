
element_one = input('Введите элементы 1го списка через запятую: ')
elements_one = set(element_one.replace(' ', '').split(','))

if len(elements_one) <= 1:
    counter = True
    while counter:
        print(elements_one)
        element_one = input('Хотите Ввести еще элементы 1го списка?: ')
        if element_one == '':
            counter = False
        else:
            element_one = set(element_one.replace(' ', '').split(','))
            elements_one.update(element_one)

element_two = input('Введите элементы 2го списка через запятую: ')
elements_two = set(element_two.replace(' ', '').split(','))
print('Результат: ', end='')
print(*(elements_one.difference(elements_two)), sep=', ')

