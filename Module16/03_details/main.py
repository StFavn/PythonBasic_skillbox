def count_detail(list_shop):
    num, summa = 0, 0
    for detail in list_shop:
        if detail[0] == name_detail:
            num += 1
            summa += detail[1]
    return num, summa


shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

name_detail = input('Название детали: ')
num_detail, summa_cost = count_detail(shop)
print('Кол-во деталей —', num_detail)
print('Общая стоимость —', summa_cost)