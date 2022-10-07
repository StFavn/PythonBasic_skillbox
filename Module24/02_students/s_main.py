class Student:
    def __init__(self, name='', group=0, efficiency=[] ) -> None:
        self.name = name
        self.group = group
        self.efficiency = efficiency
    
    def print_data(self):
        print(self.name, self.group, self.efficiency)
        