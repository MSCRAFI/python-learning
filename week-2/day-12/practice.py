# JSON handling in Python

import json

# Sample data to be written to a JSON file
data = {
    "students": [
        {"name": "Alice", "age": 20, "grade": "A"},
        {"name": "Bob", "age": 19, "grade": "B"},
        {"name": "Charlie", "age": 21, "grade": "A"}
    ]
}

# Convert Python object to JSON string
json_string = json.dumps(data, indent=4)  # Convert Python object to JSON string with indentation
print(f"JSON String:\n{json_string}")

json_data = '{"students": [{"name": "Alice", "age": 20, "grade": "A"}, {"name": "Bob", "age": 19, "grade": "B"}, {"name": "Charlie", "age": 21, "grade": "A"}]}'  # Example JSON string
# Convert JSON string back to Python object
python_obj = json.loads(json_data)
print(f"Python Object:\n{python_obj}")

# Writing data to a JSON file
with open('student.json', 'w') as f:
    json.dump(data, f, indent=4)

# Reading data from a JSON file
with open('student.json', 'r') as f:
    data_from_file = json.load(f)
    print(f"Data read from JSON file:\n{data_from_file}")