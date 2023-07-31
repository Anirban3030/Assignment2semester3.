#7. Check if two sets have any elements in common. If yes, display the common elements.
if __name__ == "__main__":
    # Get user input for the first set of elements separated by commas
    n = input("Enter the elements of the first set separated by commas: ")

    # Convert the input string into a set
    set1 = set(n.split(','))

    # Get user input for the second set of elements separated by commas
    m = input("Enter the elements of the second set separated by commas: ")

    # Convert the input string into a set
    set2 = set(m.split(','))

    # Find the common elements between the two sets using the & operator
    common_elements = set1 & set2

    if common_elements:
        print("Common elements between the two sets:", common_elements)
    else:
        print("The sets have no elements in common.")
