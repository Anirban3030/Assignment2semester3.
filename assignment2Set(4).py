#4. Update the first set with items that don’t exist in the second set. 
if __name__ == "__main__":
    set1_input = input("Enter the elements of the first set separated by commas: ")
    set1 = set(set1_input.split(','))
    set2_input = input("Enter the elements of the second set separated by commas: ")
    set2 = set(set2_input.split(','))
    difference_items = set1.difference(set2)
    set1.update(difference_items)
    print("First set after updating:", set1)
