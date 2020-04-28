"""По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
проходящей через эти точки"""

x = input('enter coordinates for x with space between: ')
y = input('enter coordinates for y with space between: ')

replacements = (',', '/', '\\', '-', '!', '?')
for r in replacements:
    x = x.replace(r, '.')
    y = y.replace(r, '.')
y = y.split()
x = x.split()
x1, x2 = float(x[0]), float(x[1])
y1, y2 = float(y[0]), float(y[1])
k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
print(f'for coordinates x({x1}, {x2}), coordinates y({y1}, {y2}): y = {k}x + {b}')
