import random

summa = 0
try:
    with open('out_file.txt', 'w') as out_file:
        while summa < 777:
            number = int(input('Введите число: '))
            summa += number
            if random.randint(1, 13) == 1:
                raise random.choice([ValueError, TypeError, SystemError, SyntaxError, UnicodeError, OSError, NameError])
            out_file.write(str(number) + '\n')
except (ValueError, TypeError, SystemError, SyntaxError, UnicodeError, OSError, NameError):
    print('Вас постигла неудача!')
