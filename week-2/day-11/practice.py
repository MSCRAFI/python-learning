# python file handling (text & csv files)

# Writing to a text file
with open('example.txt', 'w') as file: # 'w' for write mode
    file.write("Hello, World!\n")
    file.write("This is a sample text file.\n") # close is automatic with 'with' statement

# Reading from a text file
with open('example.txt', 'r') as file: # 'r' for read mode
    content = file.read()
    print("Content of example.txt:")
    print(content)

# Appending to a text file
with open('example.txt', 'a') as file: # 'a' for append mode
    file.write("Appending a new line.\n")
# Reading the updated file
with open('example.txt', 'r') as file:
    content = file.read()
    print("Updated content of example.txt:")
    print(content)

with open("example.txt", "r") as f_in:
    content = f_in.read()

with open("output.txt", "w") as f_out:
    f_out.write(content)
