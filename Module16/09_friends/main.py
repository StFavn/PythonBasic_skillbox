def get_list_receipts(num):
    receipts = []
    for i in range(num_receipts):
        one_receipt = []
        print(f'\n{i + 1}-я расписка')
        one_receipt.append(int(input('Кому: ')))
        one_receipt.append(int(input('От кого: ')))
        while one_receipt[0] == one_receipt[1]:
            print('Нельзя задолжать самому себе.')
            one_receipt[0] = int(input('Кому: '))
            one_receipt[1] = int(input('От кого: '))
        one_receipt.append(int(input('Сколько: ')))
        receipts.append(one_receipt)
    return receipts


def get_list_balance(receipts, num):
    balance = [0] * num
    for a_friend in range(num):
        for i in range(num_receipts):
            if receipts[i][0] == a_friend + 1:
                balance[a_friend] -= receipts[i][2]
            if receipts[i][1] == a_friend + 1:
                balance[a_friend] += receipts[i][2]
    return balance


num_friends = int(input('Кол-во друзей: '))
num_receipts = int(input('Долговых расписок: '))
receipts_list = get_list_receipts(num_receipts)
balance_list = get_list_balance(receipts_list, num_friends)
print('\nБаланс друзей:')
for friend in range(num_friends):
    print(f'{friend + 1}: {balance_list[friend]}')