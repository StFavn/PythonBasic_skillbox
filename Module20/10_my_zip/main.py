def my_zip(*args):
    list_of_dict = [{key: volume for key, volume in enumerate(one_arg)} for one_arg in args]
    return (
        tuple([one_dict[i] for one_dict in list_of_dict])
        for i in
        range(min([len(one_dict) for one_dict in list_of_dict]))
    )


# user_str = 'abcd'
# user_list = [10, 20, 30, 40]
# user_tuple = (11, 22, 33, 44)
# user_dict = {'aa': 1, 'bb': 2, 'cc': 3, 'dd': 4}
#
# new_list = my_zip(user_str, user_list, user_tuple, user_dict)
#
# print(new_list)
# for pair in new_list:
#     print(pair)
