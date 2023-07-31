#count the number of occurences of the number in the tuple  
if __name__ == "__main__":
    try:
        # Get user input for the tuple
        user_input = input("Enter a tuple of elements separated by commas: ")
        
        # Convert the input string into a tuple
        user_tuple = tuple(map(str.strip, user_input.split(',')))

        # Get user input for the item to count
        item_to_count = input("Enter the item you want to count: ")

        # Call the count() method on the tuple to get the occurrences of the item
        result = user_tuple.count(item_to_count)

        print(f"The item '{item_to_count}' appears {result} times in the tuple.")
    except ValueError:
        print("Invalid input. Please provide a valid tuple.")

