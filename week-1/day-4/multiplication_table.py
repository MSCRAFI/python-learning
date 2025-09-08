# Learning Python - Loops and Control Statements - Multiplication Table

number = input("Enter a number: ")
for i in range(1, 11):
    product = int(number) * i
    print(f"{number} x {i} = {product}")