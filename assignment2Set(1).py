#1. Add a list of elements to a set 
n = input("Enter a list of elements separated by commas: ")
list = n.split(',')
set = set(list)
print("The elements have been added to the set:", set)
