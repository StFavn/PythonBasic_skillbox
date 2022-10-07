order_data = dict()
for i in range(1, 1 + int(input('Введите количество заказов: '))):
    order = input(f'{i}-й заказ: ').split()

    while len(order) < 3:
        order = input('"заказчик пицца количество": ').split()

    if not order_data.get(order[0]):
        order_data[order[0]] = dict()
    if order_data[order[0]].get(order[1]):
        order_data[order[0]][order[1]] += int(order[2])
    else:
        order_data[order[0]][order[1]] = int(order[2])

print()
for customer, details in sorted(order_data.items()):
    print(f'{customer:}')
    for name_pizza, num in sorted(details.items()):
        print(f'\t{name_pizza}: {num}')
