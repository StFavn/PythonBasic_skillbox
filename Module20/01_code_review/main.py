students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def interests_and_length(data_students):
    return set([interest for info in data_students.values() for interest in info['interests']]), \
           len(''.join([info['surname'] for info in data_students.values()]))


print('\nСписок пар "ID студента — возраст":', [(id_stud, info['age']) for id_stud, info in students.items()])

list_interests, length_surname = interests_and_length(students)
print('\nПолный список интересов всех студентов:', list_interests)
print('Общая длина всех фамилий студентов:', length_surname)
