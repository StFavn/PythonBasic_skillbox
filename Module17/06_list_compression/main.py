import random

N = int(input('Количество чисел в списке: '))
list_elements = [random.randint(0, 2) for _ in range(N)]
print('\nСписок до сжатия:', list_elements)

num_zero = list_elements.count(0)
for _ in range(num_zero):
    list_elements.remove(0)
    list_elements.append(0)

print('Список после сжатия:', list_elements[:N - num_zero])
