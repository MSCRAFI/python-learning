# find max in a list of numbers
numbers = [10, 3, 6, 2, 8, 4, 11, 5, 9, 7]
max = numbers[0]
for i in numbers:
    if i > max:
        max = i
print(f"The largest number is {max}")