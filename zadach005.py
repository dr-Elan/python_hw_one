a_x = int(input('Введите координату X первой точки: '))
a_y = int(input('Введите координату Y первой точки: '))
b_x = int(input('Введите координату X второй точки: '))
b_y = int(input('Введите координату Y второй точки: '))

length_btw_pnts = ((a_x - b_x)**2 + (a_y - b_y)**2)**(0.5)
print('расстояние между точками равно: ', length_btw_pnts)