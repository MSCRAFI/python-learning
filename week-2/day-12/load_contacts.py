# python program to read contacts from a json file and display the phone number of a given contact name

import json

with open('contacts.json', 'r') as f:
    contacts = json.load(f)
    # Display all contacts
    print(f"All Contacts: {contacts}")
    # lowercase contact names
    contacts = {k.lower(): v for k, v in contacts.items()} # create a new dictionary with lowercase keys
    name = input("Enter contact name to search: ")
    phone = contacts.get(name)
    if phone:
        print(f"Phone number of {name} is {phone}")
    else:
        print(f"Contact {name} not found.")