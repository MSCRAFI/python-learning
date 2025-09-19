# python reviewing tricky topics (loops, dicts, OOP)

# 1. Write a function that takes a list of integers and returns a new list with only the even numbers.
def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]
print(filter_even_numbers([1, 2, 3, 4, 5, 6]))  # Output: [2, 4, 6]

# 2. Create a class called "Circle" that has an attribute for radius and a method to calculate the circumference of the circle.
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * math.pi * self.radius

circle = Circle(7)
print(circle.circumference())  # Output: 43.982297150257104

# 3. Write a function that takes a string as input and returns the string with all vowels removed.
def remove_vowels(input_string):
    vowels = 'aeiou'
    return ''.join([char for char in input_string.lower() if char not in vowels])

print(remove_vowels("Hello World"))  # Output: Hll Wrld

# 4. Write a function that takes a list of integers and returns the sum of all the even numbers.
def sum_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

print(sum_even_numbers([1, 2, 3, 4, 5, 6]))  # Output: 12

# 5. Loops, Dicts, OOP
# 5.1 Loops
for i in range(5):
    print(i)  # Output: 0 1 2 3 4

for i in range(5):
    print(i, end=" ")  # Output: 0 1 2 3 4

for i in range(5):
    print(i, end=" ")  # Output: 0 1 2 3 4
    print(i * 2)  # Output: 0 2 4 6 8

# 5.2 Dicts
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict['name'])  # Output: John
print(my_dict.get('age'))  # Output: 30
print(my_dict.get('state'))  # Output: None

my_dict.update({'state': 'California'})
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'state': 'California'}

# 5.3 OOP
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person = Person("John", 30)
person.greet()  # Output: Hello, my name is John and I am 30 years old.

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def study(self):
        print(f"I am studying for my {self.grade} grade.")

student = Student("John", 20, "A")
student.greet()  # Output: Hello, my name is John and I am 20 years old.
student.study()  # Output: I am studying for my A grade.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle = Rectangle(5, 3)
print(rectangle.area())  # Output: 15
print(rectangle.perimeter())  # Output: 16

# 6. Functions
def greet(name):
    print(f"Hello, {name}!")

greet("John")  # Output: Hello, John!

def add(a, b):
    return a + b

print(add(2, 3))  # Output: 5

def multiply(a, b):
    return a * b

print(multiply(2, 3))  # Output: 6

def calculate_area(width, height):
    return width * height

print(calculate_area(5, 3))  # Output: 15