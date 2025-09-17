# python program to save dictionary contacts to a file using JSON

import json

number = int(input("How many contacts do you want to save? "))
contacts = {}
for i in range(number):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contacts[name] = phone

with open('contacts.json', 'w') as f:
    json.dump(contacts, f, indent=4)
    f.write("\n")  # Add a newline for better readability if appending multiple times