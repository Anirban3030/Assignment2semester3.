#3. Get Only unique items from two sets.
set1_input = input("Enter the elements of the first set separated by commas: ")
set1 = set(set1_input.split(','))
set2_input = input("Enter the elements of the second set separated by commas: ")
set2 = set(set2_input.split(','))
unique_items = set1 | set2
print("Unique items from both sets:", unique_items)
