def collect_reverse_message(mes):
    reverse_mes, word = '', ''
    for sym in mes:
        if sym.isalpha():
            word = sym + word
        else:
            reverse_mes += word + sym
            word = ''
    reverse_mes += word
    return reverse_mes


message = input('Сообщение: ')
print('Новое сообщение:', collect_reverse_message(message))

# Опять не смог придумать ничего лучше(
