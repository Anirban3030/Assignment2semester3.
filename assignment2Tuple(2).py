#2. Access value 20 from the tuple. 

n = int(input("Enter the number of elements in the list: "))
list = []
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    list.append(element)  
Tuple = tuple(int(i) for i in list)   
print(Tuple)

index = Tuple.index(20)
value = Tuple[index]
print("Value 20:", value)
