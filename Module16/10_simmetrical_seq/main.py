def check_sequence(sequence):
    flip_sequence = []
    for i in range(len(sequence) - 1, -1, -1):
        flip_sequence.append(sequence[i])
    if sequence == flip_sequence:
        return False
    return True


def symmetrization(sequence):
    addition = []
    num = 0
    while check_sequence(sequence):
        sequence.insert(len(sequence) - num, sequence[num])
        addition.insert(0, sequence[num])
        num += 1
    return addition, num


N = int(input('Кол-во чисел: '))
sequence = []
for _ in range(N):
    sequence.append(int(input('Число: ')))
print('\nПоследовательность:', sequence)
addition, num = symmetrization(sequence)
print('Нужно приписать чисел:', num)
print('Сами числа:', addition)

