#4. Concatenate two lists in the following order.
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
concat = list1 +list2
print(concat)