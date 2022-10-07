import random


def get_name():
    surname = random.choice(['Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Васильев', 'Петров', 'Львов', 'Ощепков'])
    if random.randint(0, 1):
        surname_end = ''
        first_name = random.choice(['Александр', 'Дмитрий', 'Максим', 'Сергей', 'Артём', 'Алексей', 'Андрей', 'Ефрем'])
    else:
        surname_end = 'a'
        first_name = random.choice(['Анастасия', 'Анна', 'Мария', 'Елена', 'Дарья', 'Алина', 'Ирина', 'Екатерина'])
    return surname + surname_end + ' ' + first_name


class Student:
    def __init__(self, name='', number_group=0, efficiency=None):
        self.name = name
        self.number_group = number_group
        self.efficiency = efficiency

    def print_data(self):
        print(self.name.center(20), self.number_group, self.efficiency)

    def average_score(self):
        return sum(self.efficiency) / len(self.efficiency)


list_students = [
    Student(get_name(), random.randint(1, 2) + 22300, [random.randint(3, 5) for _ in range(5)]) for _ in range(10)]

list_students = sorted(list_students, key=lambda stud: stud.average_score())

for student in list_students:
    student.print_data()