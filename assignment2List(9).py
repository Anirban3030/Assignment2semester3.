#9.Replace list’s item with new value if found
list = [2,4,6,8,10,12] 
ovalue = int(input("Enterthe no. want to replace: ")) 
newvalue = int (input("Enter the new value: ")) 
if ovalue in list:
    index = list.index(ovalue)
    list[index] = newvalue
print(list)