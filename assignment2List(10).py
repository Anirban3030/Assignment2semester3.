#10. Remove all occurrences of a specific item from a list. 
# Sample list
my_list = [1, 2, 3, 2, 4, 5, 2]

# Item to remove
item_to_remove = 2

# Remove all occurrences of the item using the remove() method in a loop
while item_to_remove in my_list:
    my_list.remove(item_to_remove)

# Print the updated list
print("Updated list:", my_list)
