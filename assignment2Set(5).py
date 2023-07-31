# 5. Remove items from the set at once.
set_input = input("Enter the elements of the set separated by commas: ")
set1 = set(set_input.split(','))
remove_input = input("Enter the items to remove separated by commas: ")
items = set(remove_input.split(','))
set1 -= items
print("Updated set:", set1)
