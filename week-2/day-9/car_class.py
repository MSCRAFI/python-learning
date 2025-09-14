# python class to represent a car

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"
    
    def __repr__(self):
        return f"Car(brand={self.brand!r}, model={self.model!r}, year={self.year})"
    
my_car = Car("Toyota", "Corolla", 2020)
print(my_car.display_info())  # Output: 2020 Toyota Corolla
print(my_car)  # Output: Car(brand='Toyota', model='Corolla', year=2020)