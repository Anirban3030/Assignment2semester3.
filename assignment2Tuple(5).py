#5. Swap two tuples in Python  
# Two tuples to swap
n = int(input("Enter the number of elements in the list: "))
list = []
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    list.append(element)  
tuple1 = tuple(int(i) for i in list)   
print(tuple1) 
m = int(input("Enter the number of elements in the list: "))
list2 = []
for i in range(m):
    element2 = input(f"Enter element {i+1}: ")
    list2.append(element2)  
tuple2= tuple(int(i) for i in list2)   
print(tuple2)
temp = tuple1
tuple1 = tuple2
tuple2 = temp

print("Swapped tuple1:", tuple1)
print("Swapped tuple2:", tuple2)
