#2. Return a new set of identical items from two sets. 
n = input("Enter the elements of the first set separated by commas: ")
set1 = set(n.split(','))
m = input("Enter the elements of the second set separated by commas: ")
set2 = set(m.split(','))
identicalitems = set1 & set2
print("Identical items in both sets:", identicalitems)
