# Learning Python - Functions

def greet(): # function definition
    print("Hello World!")

greet()

def greeting(name): # function with parameter
    print(f"Hello, {name}, welcome to Python!")

greeting("Alice")

def add_numbers(a, b): # function with multiple parameters
    print(a + b)

add_numbers(5, 10)
add_numbers(20, 30)

def add_and_return(a, b): # function that returns a value
    return a + b

result = add_and_return(15, 25)
print(f"The sum is {result}")
print(f"{result * 2}")

def greeting_with_default(name="Guest"): # function with default parameter
    print(f"Hello, {name}, welcome to Python!")

greeting_with_default()