#8. Update set1 by adding items from set2, except common items.
if __name__ == "__main__":
    # Get user input for the first set of elements separated by commas
    set1_input = input("Enter the elements of the first set separated by commas: ")

    # Convert the input string into a set
    set1 = set(set1_input.split(','))

    # Get user input for the second set of elements separated by commas
    set2_input = input("Enter the elements of the second set separated by commas: ")

    # Convert the input string into a set
    set2 = set(set2_input.split(','))

    # Find the elements in set1 or set2 but not both using the ^ operator
    elements_to_print = set1 ^ set2

    print("Elements from set1 and set2 (excluding common elements):", elements_to_print)
