"""Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)."""
a = int(input('enter number 1: '))
b = int(input('enter number 2: '))
c = int(input('enter number 3: '))
average = int
try:
    if a != b != c:
        if b < a < c or c < a < b:
            average = a
        elif a < b < c or c < b < a:
            average = b
        else:
            average = c
        print(f'average is {average}')
    else:
        print("there's no average if some of 3 numbers are equal")
except:
    print('check data and try again')