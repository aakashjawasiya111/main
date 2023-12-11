class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f"<Car {self.make} {self.model}>"


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_cars(self,car):
        if not isinstance(car, Car):
            raise TypeError(f'Tried to add a {car.__class__.__name__} to the garage , but you can only add Cars')
        self.cars.append(car)


ford = Garage()
car= Car('ford', 'fiesta')
ford.add_cars(car)
print(len(ford))
# print(repr(car))
print(car)