import random
N = int(input('Введите максимальное число: '))
hidden_number = str(random.randint(1, N))

possible_answers = set()
for i in range(1, 1 + N):
    possible_answers.add(str(i))

while True:
    numbers_guess = input('\nНужное число есть среди вот этих чисел: ').split()
    if ''.join(numbers_guess).lower() == 'помогите!':
        break
    if hidden_number in numbers_guess:
        print('Ответ Артёма: Да')
        possible_answers &= set(numbers_guess)
    else:
        print('Ответ Артёма: Нет')
        possible_answers -= set(numbers_guess)

print('Артём мог загадать следующие числа:', ', '.join(list(sorted(possible_answers, key=str))))
