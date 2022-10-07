def add_guest(guests_list):
    name_guest = input('Имя гостя: ')
    if len(guests) < 6:
        print('Привет, ' + name_guest + '!')
        guests_list.append(name_guest)
    else:
        print('Прости, ' + name_guest + ', но мест нет.')


def delete_guest(guests_list):
    name_guest = input('Имя гостя: ')
    if name_guest in guests_list:
        print('Пока, ' + name_guest + '!')
        guests_list.remove(name_guest)
    else:
        print('На вечеринке и так нет человека с именем "' + name_guest + '"')


guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('\nСейчас на вечеринке', len(guests), 'человек')
    change = input('Гость пришёл или ушёл? ')
    if change == 'пришёл':
        add_guest(guests)
    elif change == 'ушёл':
        delete_guest(guests)
    elif change == 'Пора спать':
        print('\nВечеринка закончилась, все легли спать.')
        break
    else:
        print('Не понятно, что вы говорите: "ушёл", "пришёл" или "Пора спать"?')
