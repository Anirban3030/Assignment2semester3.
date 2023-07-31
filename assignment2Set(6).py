#6. Return a set of elements present in Set A or B, but not both.
set1_input = input("Enter the elements of the first set separated by commas: ")
set1 = set(set1_input.split(','))
set2_input = input("Enter the elements of the second set separated by commas: ")
set2 = set(set2_input.split(','))
result_set = set1 ^ set2
print("Elements present in Set A or B, but not both:", result_set)
