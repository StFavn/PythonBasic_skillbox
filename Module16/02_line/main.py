def init_row(a, b, step):
    return list(range(a, b + 1, step))


fir_row = init_row(160, 176, 2)
sec_row = init_row(162, 180, 3)
fir_row.extend(sec_row)
fir_row.sort
print('Отсортированный список учеников:', fir_row)
