# python program to write numbers from 1 to 100 into a text file

with open("numbers.txt", "w") as f:
    for i in range(1, 101):
        f.write(f"{i}\n")