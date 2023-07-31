#6. Remove empty strings from the list of strings. 
list = ["", "Hello", "", "Python", ""]
print("Original list is : " + str(list))
while("" in list):
	list.remove("")
print("Modified list is : " + str(list))
