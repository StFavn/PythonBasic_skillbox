sample = input('Введите строку: ')
letters = set([sym for sym in sample])
parity_nums_letter = [sample.count(letter) % 2 for letter in letters]
if parity_nums_letter.count(1) <= 1:
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')
