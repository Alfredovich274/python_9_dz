entered_digits = input('Введите элементы списка через запятую: ')
entered_digits = entered_digits.replace(" ", '').replace(';', ',').\
    replace('/', ',').split(',')
unique_numbers = set(entered_digits)
print('Результат: ', end='')
print(*unique_numbers, sep=', ')
