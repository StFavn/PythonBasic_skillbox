def is_prime(num):
    if num < 2:
        return False
    for divider in range(2, num):
        if num % divider == 0:
            return False
    return True


def universal_trans_pair(user_collection):
    if isinstance(user_collection, dict):
        user_collection = user_collection.items()
    return user_collection


def crypto(user_collection):
    return [value for index, value in enumerate(universal_trans_pair(user_collection)) if is_prime(index)]


data = [str(i) for i in range(10)]  # Для проверки
print(crypto(data))
print(crypto(''.join(data)))
print(crypto(sorted(set(data), key=str)))
print(crypto({i: data[i] for i in range(len(data))}))
print(crypto(tuple(data)))
