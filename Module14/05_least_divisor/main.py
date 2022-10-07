def find_min_divider(N):
    num  = 2
    lim = N
    while num <= lim:
        lim = N // num
        if N % num == 0:
            return num
        num += 1
    else:
        return N

N = int(input('Введите число: '))
while N < 0:
    N = int(input('Положительное число: '))

print('Наименьший делитель, отличный от единицы:', find_min_divider(N))