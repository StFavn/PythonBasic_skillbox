def calculating_math_func(data, calculated_dict={}):

    if data in calculated_dict:
        result = calculated_dict[data]
    else:
        result = 1
        for index in range(1, data + 1):
            result *= index
        calculated_dict[data] = result

    result /= data ** 3
    result = result ** 10
    return result
