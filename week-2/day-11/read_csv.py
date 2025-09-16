# Read and display contents of a CSV file using csv.DictReader

import csv

with open("students_marks.csv", "r") as f:
    reader = csv.DictReader(f)
    roll = 0
    for row in reader:
        roll += 1
        print(f"Roll No: {roll}, Name: {row['Name']}, Math Marks: {row['Math']}, Science Marks: {row['Science']}, English Marks: {row['English']}")