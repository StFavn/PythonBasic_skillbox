def tpl_sort(user_tuple):

    for elem in user_tuple:
        if type(elem) != int:
            return user_tuple

    return tuple(sorted(list(user_tuple)))


# print(tpl_sort(tuple([6, 3, -1, 8, 4, 10, -5])))
