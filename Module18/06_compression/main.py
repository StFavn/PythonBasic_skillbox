def encoding(user_str):
    the_sym, encoding_str, num = user_str[0], '', 0
    for sym in user_str:
        if the_sym == sym:
            num += 1
        else:
            encoding_str += the_sym + str(num)
            the_sym, num = sym, 1
    encoding_str += the_sym + str(num)
    return encoding_str


begin_str = input('Введите строку: ')
print('Закодированная строка:', encoding(begin_str))

# Не смог придумать ничего лучше(
