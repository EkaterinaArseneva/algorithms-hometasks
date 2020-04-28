"""По введенным пользователем длинам трех отрезков определить, можно ли составить из этих отрезков треугольник.
Если да, определить, будет ли треугольник разносторонним, равнобедренным или равносторонним.
"""
a = float(input('enter length of 1sr side: '))
b = float(input('enter length of 2nd side: '))
c = float(input('enter length of 3rd side: '))

if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        print('triangle is possible')
        if a == b == c:
            print('triangle is equilateral')
        elif a == b or a == c or b == c:
            print('triangle is isosceles')
        else:
            print('triangle is scalene')
    else:
        print('triangle is not possible')
else:
    print('data is incorrect, enter valid numbers > 0')