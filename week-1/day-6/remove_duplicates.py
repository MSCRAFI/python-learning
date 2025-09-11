# removing duplicates from a list using sets

items = [1, 2, 2, 3, 4, 4, 5]
unique_items = set(items)
print(f"Original list: {items}")
print(f"List after removing duplicates: {list(unique_items)}")