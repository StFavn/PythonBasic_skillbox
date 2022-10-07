import random

fst_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
sec_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
list_winners = [max(fst_team[i], sec_team[i]) for i in range(20)]

print('Первая команда:', fst_team)
print('Вторая команда:', sec_team)
print('Победители тура:', list_winners)