class Parent:
    def __init__(self, name='', age=16, children=None):
        self.name = name
        self.age = age
        if all(self.age - child.age >= 16 for child in children):
            self.children = children
        else:
            self.children = []
            print('Too young for such children.')

    def self_info(self):
        print('Parent: {}, age: {}, children:'.format(self.name, self.age))
        for child in self.children:
            child.self_info()

    def get_calm(self):
        for child in self.children:
            if child.calm < 4:
                child.calm += 1

    def feed_children(self):
        for child in self.children:
            if child.hunger < 4 and child.calm != 4:
                child.hunger += 1


class Child:
    list_calm = ['monster', 'scream', 'impatient', 'restful', 'sleep']
    list_hunger = ['half dead', 'ketosis', 'hunger', 'full', 'overeat']

    def __init__(self, name='', age=0, calm=0, hunger=0):
        self.name = name
        self.age = age
        self.calm = calm
        self.hunger = hunger

    def self_info(self):
        print('Child {}, age {}, calm: {}, hunger: {}'.format(
            self.name, self.age, Child.list_calm[self.calm], Child.list_hunger[self.hunger]))
