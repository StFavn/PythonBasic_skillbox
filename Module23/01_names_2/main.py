
with open('people.txt', 'r', encoding='utf8') as peoples, open('errors.log', 'wb') as log_file:
    summa, number = 0, 0
    for line in peoples:
        number += 1
        clear_line_len = len(line.rstrip())
        summa += clear_line_len
        try:
            if clear_line_len < 3:
                raise Exception('В строке номер {num}: "{str}" количество знаков лишь: {length} .'.format(
                    num=number,
                    str=line.rstrip(),
                    length=clear_line_len
                ))
        except Exception as exc:
            log_file.write(str(exc).encode('utf-8'))

    print('Суммарно всех знаков:', summa)
