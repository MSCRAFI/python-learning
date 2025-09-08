# Learning Python - Loops and Control Statements - Sum of numbers from 1 to user input

number = int(input("Enter a number: "))
sum = 0
for i in range(number + 1):
    sum = sum + i
print(f"The sum of {number} and 100 is {sum}")