def check_num_people(roller_skates_list, foot_sizes_list):
    roller_skates_list.sort()
    foot_sizes_list.sort()
    num = 0
    for size in foot_sizes_list:
        for roller_skate in roller_skates_list:
            if roller_skate >= size:
                num += 1
                roller_skates_list.remove(roller_skate)
                break
    return num


def filling_list(str_for_num, str_for_filling):
    return [int(input(str_for_filling.format(i=i))) for i in
            range(1, 1 + int(input(str_for_num)))]


roller_skates = filling_list('\nКол-во коньков: ', 'Размер {i}-й пары: ')
foot_sizes = filling_list('\nКол-во людей: ', 'Размер ноги {i}-го человека: ')

people = check_num_people(roller_skates, foot_sizes)
print('\nНаибольшее кол-во людей, которые могут взять ролики:', people)