# going deeper into functions

def introduce_yourself(name, age, city):
    print(f"Hello, my name is {name}. I'm {age} years old and I live in {city}.")

# positional arguments (order matters)
introduce_yourself("Bob", 30, "New York")

# keyword arguments (order doesn't matter)
introduce_yourself(age=25, city="Los Angeles", name="Alice")

def factorial(n):
    if n == 0 or n ==1:
        return 1
    return n * factorial(n - 1)

print(f"Factorial of 5 is {factorial(5)}")
print(f"Factorial of 5 is {factorial(2)}")
print(f"Factorial of 0 is {factorial(0)}")
print(f"Factorial of 7 is {factorial(7)}")

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Fibonacci of 5 is {fibonacci(5)}")
print(f"Fibonacci of 10 is {fibonacci(10)}")
print(f"Fibonacci of 0 is {fibonacci(0)}")
print(f"Fibonacci of 7 is {fibonacci(7)}")

def recursive_sum(n):
    if n <= 1:
        return 1
    return n + recursive_sum(n - 1)

print(f"Sum of first 5 natural numbers is {recursive_sum(5)}")
print(f"Sum of first 10 natural numbers is {recursive_sum(10)}")
print(f"Sum of first 1 natural number is {recursive_sum(1)}")