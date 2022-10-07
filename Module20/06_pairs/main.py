import random

num = 10
original_list = [random.randint(1, num) for _ in range(num)]
print('Оригинальный список:', original_list)

# new_list = [(original_list[i], original_list[i + 1]) for i in range(0, num, 2)]
# new_list = [tuple(original_list[2 * i: 2 * i + 2]) for i in range(num // 2)]
# new_list = [(original_list.pop(0), original_list.pop(0)) for _ in range(num // 2)]  # Не, ну это совсем плохо
# new_list = list(zip(original_list[::2], original_list[1::2]))
new_list = list(zip(*[iter(original_list)] * 2))

print('Новый список:', new_list)
