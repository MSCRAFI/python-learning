# python more oop basics - inheritance

# base class
class Animal: # parent class
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."
    
# derived class
class Dog(Animal): # child class inheriting from Animal
    def fetch(self): # overriding the speak method
        return f"{self.name} says Woof!"
    
class Cat(Animal): # another child class inheriting from Animal
    def speak(self): # overriding the speak method
        return f"{self.name} says Meow!"
    
# creating instances of the derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Buddy makes a sound.
print(dog.fetch())  # Buddy says Woof!
print(cat.speak())  # Whiskers says Meow!

# using super() to call parent class methods

class Bird(Animal):
    def speak(self):
        base = super().speak()
        return base + f" Also, {self.name} says Chirp!"
    
bird = Bird("Tweety")
print(bird.speak())  # Tweety makes a sound. Also, Tweety says Chirp!

# inheriting __init__ and adding new attributes

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand) # call parent constructor
        self.model = model

car = Car("Toyota", "Corolla")
print(f"Car brand: {car.brand}, model: {car.model}")  # Car brand: Toyota, model: Corolla


# composition - using classes as attributes

class Engine:
    def start(self):
        return "Engine started."
    
class Truck:
    def __init__(self, brand):
        self.brand = brand
        self.engine = Engine() # Composition: Truck has an Engine

    def drive(self):
        return f"{self.brand} truck is driving. {self.engine.start()}"
    
truck = Truck("Ford")
print(truck.drive())  # Ford truck is driving. Engine started.