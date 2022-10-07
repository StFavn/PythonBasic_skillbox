fst_str = input('Первая строка: ')
sec_str = input('Вторая строка: ')

length = len(fst_str)
for k in range(length):
    if sec_str == ''.join([fst_str[(i+k) % length] for i in range(length)]):
        print('\nПервая строка получается из второй со сдвигом', k)
        break
else:
    print('\nПервую строку нельзя получить из второй с помощью циклического сдвига.')

