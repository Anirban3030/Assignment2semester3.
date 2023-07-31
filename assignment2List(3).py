n = int(input("Enter the number of elements in the list: "))
list = []
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    list.append(element)

print(list)

sqlist = [int(item) ** 2 for item in list]

print(sqlist)
