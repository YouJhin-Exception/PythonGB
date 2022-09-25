print('Введите координаты точки А:')
x_a = float(input('X: '))
y_a = float(input('Y: '))
print('Введите координаты точки B:')
x_b = float(input('X: '))
y_b = float(input('Y: '))

print(f'Расстояние между точками А и В = {round((((x_b - x_a) ** 2) + ((y_b - y_a) ** 2)) ** 0.5,2)}')

# или так dist = round(math.sqrt((x_b - x_a) ** 2 + (y_b - y_a) ** 2),2) 