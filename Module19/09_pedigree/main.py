def get_relative_height(pair_person):

    if pair_person[1] not in relative_height:
        relative_height[pair_person[1]] = 0

    relative_height[pair_person[0]] = relative_height[pair_person[1]] + 1

    if pair_person[0] in genealogy:
        for son in genealogy[pair_person[0]]:
            get_relative_height([son, pair_person[0]])


genealogy, relative_height = dict(), dict()
for i in range(1, int(input('Введите количество человек: '))):
    pair = input(f'{i}-я пара: ').split()
    if pair[1] in genealogy:
        genealogy[pair[1]].append(pair[0])
    else:
        genealogy[pair[1]] = [pair[0]]
    get_relative_height(pair)

print()
for member, height in sorted(relative_height.items()):
    print(member, height)
