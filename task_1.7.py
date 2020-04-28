"""Определить, является введённый пользователем  год високосным или нет. """
year = int(input('enter year: '))

if year >= 0:
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        print('your year is a leap year')
    else:
        print('your year is not a leap year')
else:
    print("data is incorrect, try AD")