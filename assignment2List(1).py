# 1. Reverse a list in Python 
n = int(input("Enter the number of elements in the list: "))
list = []
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    list.append(element)  
print(list)
list.reverse()
print(list)