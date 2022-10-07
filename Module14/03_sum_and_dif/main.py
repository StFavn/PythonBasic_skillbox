def sum_num(N):
    sum_num = 0
    while N != 0:
        sum_num += N % 10
        N //= 10
    return sum_num

def num_num(N):
    num_num = 0
    while N != 0:
        num_num += 1
        N //= 10
    return num_num

N = int(input('Введите число: '))
while N < 0:
    N = int(input('Нет, введите неотрицательное число: '))

sum_num = sum_num(N)
print('Сумма цифр:', sum_num)
num_num = num_num(N)
print('Количество цифр в числе:', num_num)
print('Разность суммы и количества цифр:', sum_num - num_num)
