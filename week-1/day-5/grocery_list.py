# making a grocery list to add or remove items
grocery_list = []

while True:
    action = input("Would you like to add or remove an item? (add/remove/remove_duplicate/quit): ")
    if action == "add":
        item = input("Enter the item to add: ")
        grocery_list.append(item)
        print(f"{item} has been added to the list.")
        print("Current grocery list:", grocery_list)
    elif action == "remove":
        item = input("Enter the item to remove: ")
        if item in grocery_list:
            grocery_list.remove(item)
            print(f"{item} has been removed from the list.")
            print("Current grocery list:", grocery_list)
        else:
            print(f"{item} is not in the list.")
            print("Current grocery list:", grocery_list)
    elif action == "remove_duplicate":
        item = input("Enter the item to remove duplicates: ")
        if item in grocery_list:
            remove_duplicates = list(dict.fromkeys(grocery_list))
            grocery_list = remove_duplicates
            print(f"All duplicates of {item} have been removed from the list.")
            print("Current grocery list:", grocery_list)
        else:
            print(f"{item} is not in the list.")
            print("Current grocery list:", grocery_list)
    elif action == "quit":
        break
    else:
        print("Invalid action. Please enter 'add', 'remove', or 'quit'.")