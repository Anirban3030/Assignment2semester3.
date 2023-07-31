def lists_to_dictionary(keys, values):
    return dict(zip(keys, values))

def main():
    # User input for keys list
    keys_input = input("Enter elements for keys list separated by spaces: ")
    keys_list = keys_input.split()

    # User input for values list
    values_input = input("Enter elements for values list separated by spaces: ")
    values_list = values_input.split()

    # Check if the number of keys and values is the same
    if len(keys_list) != len(values_list):
        print("Error: The number of elements in the keys list and values list must be the same.")
    else:
        result_dict = lists_to_dictionary(keys_list, values_list)
        print("Resulting dictionary:", result_dict)

if __name__ == "__main__":
    main()
