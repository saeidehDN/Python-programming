class Animal:
    def __init__(self, name, type_animal):
        self.name = name
        self.type_animal = type_animal

class Dog(Animal):
    def __init__(self, name, type_animal, color, food):
        super().__init__(name, type_animal)
        self.color = color
        self.food = food

class Cat(Animal):
    def __init__(self, name, type_animal, color, food):
        super().__init__(name, type_animal)
        self.color = color
        self.food = food


dog = Dog('max', 'poodle', 'brown', 'meat')
cat = Cat('kitty', 'scottish cat', 'gray', 'fish')


print(f'{dog.name} is a {dog.type_animal}, his color is {dog.color} and that eat {dog.food}')
print(f'{cat.name} is a {cat.type_animal}, her color is {cat.color} and that eat {cat.food}')
