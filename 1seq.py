number_elements = int(input('Введите количество элементов: '))
elements = []
for i in range(number_elements):
    element = int(input(f'Введите {i + 1} элемент: '))
    elements.append(element)
elements.sort()
print(elements)
