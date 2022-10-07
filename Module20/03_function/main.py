def slicer(user_tuple, num):
    if num not in user_tuple:
        return tuple()
    elif user_tuple.count(num) == 1:
        return user_tuple[user_tuple.index(num):]
    else:
        fst_index_num = user_tuple.index(num)
        return user_tuple[fst_index_num: user_tuple.index(num, fst_index_num + 1) + 1]


# print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
