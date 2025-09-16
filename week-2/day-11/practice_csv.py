import csv

# Writing to a CSV file
with open('students.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'age', 'grade'] # define column names
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames) # create a writer object
    
    writer.writeheader() # write the header row
    writer.writerow({'name': 'Alice', 'age': 20, 'grade': 'A'}) # write a data row
    writer.writerow({'name': 'Bob', 'age': 19, 'grade': 'B'})
    writer.writerow({'name': 'Charlie', 'age': 21, 'grade': 'A'})

# Appending to a CSV file
with open('students.csv', 'a', newline='') as csvfile:
    fieldnames = ['name', 'age', 'grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writerow({'name': 'Diana', 'age': 22, 'grade': 'B'}) # append a new row

# Reading from a CSV file
with open('students.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile) # create a reader object
    print("Students data from CSV:")
    for i in reader:
        print(f"Name: {i['name']}, Age: {i['age']}, Grade: {i['grade']}")
