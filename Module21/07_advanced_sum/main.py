def sum(*args):
    result = 0
    for one_arg in args:
        if isinstance(one_arg, list):
            for summand in one_arg:
                result += sum(summand)
        else:
            result += one_arg
    return result


# print(sum([[1, 2, [3]], [1], 3]))
# print(sum(1, 2, 3, 4, 5))
