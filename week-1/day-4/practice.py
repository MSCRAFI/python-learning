# Learning Python - Loops and Control Statements

for n in range(10):
    print(n+1, end=" ")
print()  # for newline
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1

print()  # for newline
i = 1
while 1:
    print(i, end=" ")
    if i >= 10:
        break
    i += 1

print()  # for newline

for n in range(10):
    if n == 4:
        break
    print(n+1, end=" ")
print()  # for newline

for n in range(1, 11):
    if n == 5:
        continue
    print(n, end=" ")
print()  # for newline
