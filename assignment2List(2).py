#2. Concatenate two lists index-wise.  
n= int(input("Enter the number of the elements in list1 : "))
m= int(input("Enter the number of the elements in list2 : "))
list1=[] 
list2=[] 
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    list1.append(element)  
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    list2.append(element)   
concatenated_list = [x + y for x, y in zip(list1, list2)]


print("Concatenated list:", concatenated_list)

