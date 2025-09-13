# python program to calculate the factorial of a number using recursive function.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(f"Factorial of 5 is {factorial(5)}")  # Output: 120
number = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {number} is {factorial(number)}")