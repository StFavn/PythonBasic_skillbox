def search(x, y, r):
  if x**2 + y**2 <= r**2:
    print('Монетка где-то рядом')
  else:
    print('Монетки в области нет')

print('Введите координаты металлоискателя:')
x = float(input('X = '))
y = float(input('Y = '))
r = float(input('Введите радиус: '))
if r < 0:
  r = float(input('Радиус должен быть положительным: '))

search(x, y, r)