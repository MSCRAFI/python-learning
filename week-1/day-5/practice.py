# Practicing Python - Lists and its topics indexing, slicing and methods (append, pop, sort)

numbers = [1, 2, 3, 4, 5]
print(numbers[0])  # Indexing
print(numbers[-1])  # Negative Indexing
print(numbers[1:4])  # Slicing
print(numbers[0:4:2])  # Slicing with step

numbers.append(6)  # Adding an element to the end of the list
print(numbers)
numbers.pop()  # Removing the last element from the list
print(numbers)
numbers.sort(reverse=True)  # Sorting the list in descending order
print(numbers)
numbers.sort()  # Sorting the list in ascending order
print(numbers)