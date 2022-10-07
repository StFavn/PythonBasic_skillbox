import random


def get_name_n_surname():
    surname = random.choice(['Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Васильев', 'Петров', 'Львов', 'Ощепков'])
    if random.randint(0, 1):
        surname_ending = ''
        first_name = random.choice(['Александр', 'Дмитрий', 'Максим', 'Сергей', 'Артём', 'Алексей', 'Андрей', 'Ефрем'])
    else:
        surname_ending = 'a'
        first_name = random.choice(['Анастасия', 'Анна', 'Мария', 'Елена', 'Дарья', 'Алина', 'Ирина', 'Екатерина'])
    return surname + surname_ending, first_name


alfa, betta, limit, num = 1, 2, 100, 50  # int(input('Количество людей в базе данных: '))
data = {get_name_n_surname(): int(random.betavariate(alfa, betta) * limit) for _ in range(num)}

surname_search = input('Введите фамилию: ').title()
if surname_search.endswith('а'):
    surname_search = ''.join(list(surname_search)[: -1])

for full_name, age in data.items():
    surname, name = full_name
    if surname_search in surname:
        print(surname, name, age)

    # print(name, surname, age)  # для хохмы
# print('Средний возраст по формуле:', alfa / (alfa + betta) * limit)
# print('Средний возраст по факту:', sum([age for age in data.values()]) / num)