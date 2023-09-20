class Vehicle:
    def __init__(self, color, speed):
         self.color = color
         self.speed = speed


class Car(Vehicle):
    def __init__(self, name, color, speed, price):
        super().__init__(color, speed)
        self.name = name
        self.price = price

class Bicycle(Vehicle):
    def __init__(self, brand, color, speed, price):
        super().__init__(color, speed)
        self.brand = brand
        self.price = price


car = Car('bmw', 'black', '120', '30000')
bicycle = Bicycle('bianchi', 'white', '50', '1000')


print(f'the {car.name} car is {car.color} and speed of that car is {car.speed} km/h and it price is {car.price} dollars.')
print(f'{bicycle.brand} bicycle is {bicycle.color} and it speed is {bicycle.speed} and that price is {bicycle.price} dollars.')


