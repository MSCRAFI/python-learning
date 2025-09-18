# Review functions, OOP, file handling and JSON

# 1. Write a function that takes a list of numbers as input and returns the largest number in the list.
def find_largest_number(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
print(find_largest_number([3, 5, 2, 8, 1, 9, 17, 43]))  # Output: 8

# 2. Create a class called "Rectangle" that has attributes for width and height, and a method to calculate the area of the rectangle.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
rect = Rectangle(5, 10)
print(rect.area())  # Output: 50

# 3. Write a function that reads a text file and counts the number of words in the file.
def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return "File not found."
    
print(count_words_in_file('sample.txt'))  # Output: Number of words in sample.txt

# 4. Create a function that takes a dictionary as input and returns a new dictionary with the keys and values swapped.
def swap_dict(input_dict):
    # 1. {.....} - dictionary comprehension
    # 2. for key, value in input_dict.items() - iteration
    # 3. key, value - unpacking
    # 4. value, key - swapped

    return {value: key for key, value in input_dict.items()}
print(swap_dict({'a': 1, 'b': 2, 'c': 3}))  # Output: {1: 'a', 2: 'b', 3: 'c'}

# 5. Write a class called "Person" that has attributes for name and age, and a method to display the person's information.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"
    
person = Person("Alice", 30)
print(person.display_info())  # Output: Name: Alice, Age: 30

# 6. Create a function that takes a list of dictionaries as input and returns a list of values for a specified key.
def extract_values(dict_list, key):
    return [d[key] for d in dict_list if key in d]
print(extract_values([{'name': 'Alice'}, {'name': 'Bob'}, {'age': 30}], 'name'))  # Output: ['Alice', 'Bob']

# 7. Write a function that takes a JSON string as input and converts it to a Python dictionary.
import json
def json_to_dict(json_string):
    try:
        return json.loads(json_string)
    except json.JSONDecodeError:
        return "Invalid JSON string."
print(json_to_dict('{"name": "Alice", "age": 30}'))  # Output: {'name': 'Alice', 'age': 30}