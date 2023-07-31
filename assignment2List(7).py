#7.Add new item to list after a specified item.  
list = [1, 2, 3, 4, 5]
print(list)
num = int(input("Please enter a number to add to list:\n"))
index = int(input(f'Please enter the index \n'))
list.insert(index, num)
print(list)