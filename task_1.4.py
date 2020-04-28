"""Пользователь вводит две буквы. Определить их порядковый номер в алфавите и рассчитать число букв между ними. """

letter_1 = input('input 1st letter: ').lower()
letter_2 = input('input 2nd letter: ').lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
if letter_1 in alphabet and letter_2 in alphabet:
    position_l1, position_l2 = alphabet.index(letter_1)+1, alphabet.index(letter_2)+1
    print(f'position of 1st letter - {letter_1} is: {position_l1}, \nposition of 2nd letter - {letter_2} is: {position_l2}, '
          f'\nand there is(are) {abs(position_l2 - position_l1)-1} letter(s) between them')
else:
    print('try again, enter letters from eng alphabet by one')