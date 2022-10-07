def doing():
    text = input('\nВведите строку: ')
    if 'h' not in text:
        print('Вы не ввели "h" ни разу, надо минимум два.')
        doing()
        return
    index_begin_h = text.index('h')
    index_end_h = text.rindex('h')
    if index_begin_h == index_end_h:
        print('Вы ввели "h" всего один раз, надо минимум два.')
        doing()
        return
    print('\nРазвёрнутая последовательность между первым и последним h:',
          text[index_end_h - 1: index_begin_h: -1])


doing()