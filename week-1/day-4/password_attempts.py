# Keep asking the user for a password until they get it right. The correct password is "python123".
user_password = input("Enter the password: ")
password = "python123"

while user_password != password:
    print("Incorrect password, try again.")
    user_password = input("Enter the password: ")
print("Access granted.")