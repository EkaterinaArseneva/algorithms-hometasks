"""Пользователь вводит номер буквы в алфавите. Определить, какая это буква."""

letter = input('input eng letter: ').lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
if letter in alphabet:
    position = alphabet.index(letter)+1
    print(f'position of your letter "{letter}" is: {position}')
else:
    print('try again, enter a letter from eng alphabet')