def transformat_number(num):
    flag_integer_part, minus = 1, 0
    flip_integer_part, flip_float_part = '', ''
    if num < 0:
        num *= -1
        minus = 1
    for symbol in str(num):
        if symbol == '.':
            flag_integer_part = 0
            continue
        if flag_integer_part == 1:
            flip_integer_part = symbol + flip_integer_part
        else:
            flip_float_part = symbol + flip_float_part
    return float(flip_integer_part + '.' + flip_float_part) * (-1)**minus

N = float(input('Введите первое число: '))
flip_n = transformat_number(N)

K = float(input('Введите второе число: '))
flip_k = transformat_number(K)

print('Первое число наоборот:', flip_n)
print('Второе число наоборот:', flip_k)
print('Сумма:', flip_n + flip_k)