def fibonacci_numbers(num):
    if num < 1:
        return None
    if num in (1, 2):
        return 1
    return fibonacci_numbers(num - 1) + fibonacci_numbers(num - 2)


num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
print('Число:', fibonacci_numbers(num_pos))

# Почему при вводе только 40, программа выполняется заметно долго?  В то время как факториал считался и от 500?
