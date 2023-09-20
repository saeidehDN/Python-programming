class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def show(self):
        print(f'{self.name} is {self.age} years old and is a {self.job}')
p1 = Person('ali', '28', 'teacher')
p2 = Person('mohammad', '32', 'doctor')

p1.show()
p2.show()