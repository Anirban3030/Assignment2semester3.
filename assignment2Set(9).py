#9. Remove items from set1 that are not common to both set1 and set2.  
n = input("Enter the elements of the first set separated by commas: ")
set1 = set(n.split(','))
m = input("Enter the elements of the second set separated by commas: ")
set2 = set(m.split(','))
common_elements = set1 & set2
set1.intersection_update(common_elements)
print("Updated set1:", set1)
