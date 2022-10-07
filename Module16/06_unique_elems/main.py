def init_row(num, procedure):
    new_list = []
    for i in range(1, num + 1):
        new_list.append(int(input(f'{i}-е число {procedure}-го списка: ')))
    return new_list


def remove_unnecessary_elements(any_list):
    for element in any_list:
        for _ in range(any_list.count(element) - 1):
            any_list.remove(element)
    return any_list


first_list = init_row(3, 1)
second_list = init_row(7, 2)
print('Первый список: ', first_list)
print('Второй  список: ', second_list)
first_list.extend(second_list)
unit_list = remove_unnecessary_elements(first_list)
print('\nНовый первый список с уникальными элементами:', unit_list)