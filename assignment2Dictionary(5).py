#5. Delete a list of keys from a dictionary.
def main():
    n= input("Enter elements for the original dictionary (key:value pairs separated by commas): ")
    list= n.split(",")

    dictionary = {}
    for pair in list:
        key, value = pair.split(":")
        dictionary[key.strip()] = value.strip()

    # User input for the list of keys to delete
    keys_to_delete_input = input("Enter keys to delete (separated by spaces): ")
    keys_to_delete = keys_to_delete_input.split()

    # Delete keys from the original dictionary
    for key in keys_to_delete:
        if key in dictionary:
            del dictionary[key]

    print("Updated dictionary: ", dictionary)

if __name__ == "__main__":
    main()