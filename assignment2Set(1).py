#1. Add a list of elements to a set 
user_input = input("Enter a list of elements separated by commas: ")
user_list = user_input.split(',')
my_set = set(user_list)
print("The elements have been added to the set:", my_set)
