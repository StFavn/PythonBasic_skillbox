def game(begin, rhyme, list_rhyme):
    index_rhyme = 0
    for people in range(begin, 1, -1):
        if index_rhyme == people:
            index_rhyme %= people
        print('\nТекущий круг людей:', list_rhyme)
        print('Начало счёта с номера', list_rhyme[index_rhyme])

        index_rhyme = (index_rhyme + rhyme - 1) % people
        human_remove = list_rhyme[index_rhyme]
        print('Выбывает человек под номером', human_remove)
        list_rhyme.remove(human_remove)
    print('\nОстался человек под номером', list_rhyme[0])


begin_people = int(input('\nКол-во человек: '))
num_rhyme = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {num_rhyme}-й человек')
list_people = list(range(1, begin_people + 1))
game(begin_people, num_rhyme, list_people)

