#5. Iterate both lists simultaneously. 
list1 = [2, 4, 6, 8]
list2 = ['a', 'b', 'c', 'd']

for item1, item2 in zip(list1, list2):
    print("list1:", item1)
    print("list2:", item2)
    print() 