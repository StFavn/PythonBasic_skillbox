sticks = ['|'] * (int(input('Количество палок: ')))
for num_shot in range(1, 1 + int(input('Количество бросков: '))):
    start = int(input(f'{num_shot}-й бросок. Сбиты палки с номера: '))
    end = int(input('По номер: '))

    sticks = ["." if index in range(start - 1, end) else stick for index, stick in enumerate(sticks)]