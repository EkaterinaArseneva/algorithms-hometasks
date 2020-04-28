"""Написать программу, которая генерирует в указанном пользователем диапазоне:
случайное целое число
случайное вещественное число
случайный символ
Для каждого из трех случаев пользователь задает свои границы диапазона.
Если надо получить случайный символ от 'a' до 'f', вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

import random

borders_1 = input('enter borders for int range with space between: ')
borders_2 = input('enter borders for float range with space between: ')
borders_3 = input('enter borders for alphabet range with space between: ')

x1, y1 = int(borders_1.split()[0]), int(borders_1.split()[1])
x2, y2 = float(borders_2.split()[0]), float(borders_2.split()[1])
x3, y3 = borders_3.split()[0], borders_3.split()[1]

alphabet = 'abcdefghijklmnopqrstuvwxyz'
start_ind = min([alphabet.index(x3), alphabet.index(y3)])
stop_ind = max([alphabet.index(x3), alphabet.index(y3)])
range_3 = alphabet[start_ind:stop_ind+1]

print(f' casual int is: {random.randint(min([x1, y1]), max([x1, y1]))}')
print(f' casual float is: {random.uniform(min([x2, y2]), max([x2, y2]))}')
print(f' casual symbol is: {range_3[random.randint(0, len(range_3)-1)]}')

