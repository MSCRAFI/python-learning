# function reverses string

def reverse_string(s):
    return s[::-1]

string = input("Enter a string: ")
reversed_str = reverse_string(string)
print(f"The reverse of '{string}' is '{reversed_str}'")
# --- IGNORE ---
print(f"{reversed_str[::-1]}")