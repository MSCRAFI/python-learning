# python program to add or search names in JSON file

import json
import os

# Function to add a new contact
def add_contact(name, phone):
    contact = {"name": name, "phone": phone}
    
    if os.path.exists('address_book.json'):
        with open('address_book.json', 'r') as file:
            data = json.load(file)
    else:
        data = []
    
    data.append(contact)
    
    with open('address_book.json', 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Contact {name} added.")

# Function to search for a contact by name
def search_contact(name):
    if not os.path.exists('address_book.json'):
        return "Address book is empty."
    
    with open('address_book.json', 'r') as file:
        data = json.load(file)
    
    for contact in data:
        if contact['name'].lower() == name.lower():
            return contact['phone']
    return "Contact not found."
# Example usage
add_contact("Alice", "123-456-7890")
add_contact("Bob", "987-654-3210")
print(search_contact("Alice"))  # Output: {'name': 'Alice', 'phone':
print(search_contact("Charlie"))  # Output: Contact not found.
