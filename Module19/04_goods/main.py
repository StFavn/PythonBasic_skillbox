goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

dictionary_russian_language = {
    'штука': {
        'ед. ч.': {'И.п': 'штука', 'Р.п': 'штуки'},
        'мн. ч.': {'И.п': 'штуки', 'Р.п': 'штук'}
    },
    'рубль': {
        'ед. ч.': {'И.п': 'рубль', 'Р.п': 'рубля'},
        'мн. ч.': {'И.п': 'рубли', 'Р.п': 'рублей'}
    },
}


def get_correct_ending(num, word):
    if (num % 10) == 1 and (num % 100 // 10) != 1:
        return dictionary_russian_language[word]['ед. ч.']['И.п']
    if 1 < num % 10 < 5:
        return dictionary_russian_language[word]['ед. ч.']['Р.п']
    return dictionary_russian_language[word]['мн. ч.']['Р.п']


def get_correct_ending_2(num):
    if (num % 10) == 1 and (num % 100 // 10) != 1:
        return 'ь'
    if 1 < num % 10 < 5:
        return 'я'
    return 'ей'


for name_good, num_good in goods.items():
    quantity = sum([store[num_good][i]['quantity'] for i in range(len(store[num_good]))])
    cost = sum([store[num_good][i]['price'] * store[num_good][i]['quantity'] for i in range(len(store[num_good]))])

    print('{name_good} - {quantity} {word_quantity}, стоимость, {cost:,d} {word_cost}.'.format(
        name_good=name_good,
        quantity=quantity,
        word_quantity=get_correct_ending(quantity, 'штука'),
        cost=cost,
        word_cost=get_correct_ending(cost, 'рубль')
    ))
