def decrypt_str(user_str):
    result = 0
    minus = False
    list_objects = user_str.rstrip().split()
    try:
        if list_objects[0] == '-':
            minus = True
            list_objects = list_objects[1:]
        if len(list_objects) != 3:
            raise Exception('Неправильное количество выражений.')

        fst_num, action, sec_num = tuple(list_objects)

        if fst_num.isdigit():
            fst_num = int(fst_num) * (-1) ** minus
        else:
            raise Exception('Нераспознаваемое 1-е число.')

        if sec_num.endswith(','):
            sec_num = sec_num[: -1]
        if sec_num.isdigit():
            sec_num = int(sec_num)
        else:
            raise Exception('Нераспознаваемое 2-е число.')

        result = math_func(fst_num, action, sec_num)

    except (Exception, TypeError, IndexError) as exc:
        print('\nОбнаружена ошибка в строке: {}. '.format(user_str.rstrip()), exc)

        if input('Хотите исправить? (да/нет) - ').lower() == 'да':
            result = decrypt_str(input('Введите исправленную строку: '))
    return result


def math_func(fst_n, act, sec_n):
    if act == '+':
        return fst_n + sec_n
    elif act == '-':
        return fst_n - sec_n
    elif act == '*':
        return fst_n * sec_n
    elif act == '/':
        return fst_n / sec_n
    elif act == '//':
        return fst_n // sec_n
    elif act == '%':
        return fst_n % sec_n
    elif act == '**':
        return fst_n ** sec_n
    else:
        raise Exception('Не правильное математическое действие.')


summa = 0
with open('calc.txt', 'r') as data_nums:
    for expression in data_nums:
        summa += decrypt_str(expression)
print('\nСумма результатов:', summa)


