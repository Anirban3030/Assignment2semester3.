#6. Remove empty strings from the list of strings. 
list = ["", "GeeksforGeeks", "", "is", "best", ""]
print("Original list is : " + str(list))
while("" in list):
	list.remove("")
print("Modified list is : " + str(list))
