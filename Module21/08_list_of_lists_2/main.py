def rewrite_list(broken_list, correct_list):
    for element in broken_list:
        if isinstance(element, list):
            rewrite_list(element, correct_list)
        else:
            correct_list.append(element)


def straighten_list(broken_list):
    correct_list = []
    rewrite_list(broken_list, correct_list)

    broken_list.clear()
    for element in correct_list:
        broken_list.append(element)


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]
straighten_list(nice_list)
print(nice_list)
