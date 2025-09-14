# python oop basics - classes and objects

# class is a blueprint for creating objects
# object is an instance of a class

# class attributes are shared by all instances of a class
# instance attributes are unique to each instance


# creating a class
class Dog:
    species = "Canis familiaris"  # class attribute (common to all instances)

    def __init__(self, name, age=0): # constructor method
        self.name = name # instance attribute (unique to each instance)
        self.age = age   # instance attribute (unique to each instance)

    def bark(self): # instance method
        return f"{self.name} says Woof!"

# creating instances of the Dog class
dog1 = Dog(age=3, name="Buddy")
dog2 = Dog("Max", 5)

print(f"{dog1.name} is {dog1.age} years old and belongs to species {dog1.species}.")
print(dog1.bark())
print(f"{dog2.name} is {dog2.age} years old and belongs to species {dog2.species}.")
print(dog2.bark())

# demonstrating class vs instance attributes

a = Dog("A", 2)
b = Dog("B", 4)

Dog.species = "Canis lupus familiaris"  # change class attribute for all
print(a.species, b.species)  # both see the change
a.species = "Canis something else"  # change instance attribute for "a" only
print(a.species, b.species)  # only "a" sees the change

class Basket:
    def __init__(self, items = None):
        self.items = [] if items is None else list(items)

basket1 = Basket()
basket2 = Basket()
print(basket1.items)  # both should be empty lists
basket1.items.append("apple")
print(basket2.items)  # should still be empty, proving no shared mutable default argument

# --- IGNORE ---

# more on class methods and static methods
class Person:
    def __init__(self, first, last, birth_year):
        self.first = first
        self.last = last
        self.birth_year = birth_year

    def full_name(self):  # instance method
        return f"{self.first} {self.last}"
    
    @classmethod
    def from_full_name(cls, full_name, birth_year): # class method as alternative constructor
        first, last = full_name.split()
        return cls(first, last, birth_year)
    
    @staticmethod
    def is_adult(age): # static method
        return age >= 18

# creating instances of Person class

person1 = Person("John", "Doe", 1990)
person2 = Person.from_full_name("Jane Smith", 2008)
print(f"{person1.full_name()} is borned in {person1.birth_year}.")
print(f"{person2.full_name()} is borned in {person2.birth_year}")
print(f"Is {person1.first} an adult? {'Yes' if Person.is_adult(2024 - person1.birth_year) else 'No'}")
print(f"Is {person2.first} an adult? {'Yes' if Person.is_adult(2024 - person2.birth_year) else 'No'}")

# --- IGNORE ---


# __repr__ and __str__ methods
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self): # official string representation
        return f"Point({self.x}, {self.y})"  # unambiguous representation
    
    def __str__(self): # informal string representation
        return f"({self.x}, {self.y})"  # user-friendly representation
    
point = Point(3, 4)
print(repr(point))  # calls __repr__
print(str(point))   # calls __str__
print(point)       # calls __str__ by default

# --- IGNORE ---