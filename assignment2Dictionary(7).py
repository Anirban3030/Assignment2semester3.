#
def main():
    dict_input = input("Enter elements for the dictionary (key:value pairs separated by commas): ")
    dict_list = dict_input.split(",")
    dictionary = {}
    for pair in dict_list:
        key, value = pair.split(":")
        dictionary[key.strip()] = value.strip()
    prev_key = input("Enter the previous key: ")
    new_key = input("Enter the new key: ")

    if prev_key in dictionary:
        
        dictionary[new_key] = dictionary[prev_key]
        # Delete the old key
        del dictionary[prev_key]
        print(f"Key '{prev_key}' renamed to '{new_key}' in the dictionary.")
    else:
        print(f"Key '{prev_key}' does not exist in the dictionary.")

    print("Updated dictionary:", dictionary)

if __name__ == "__main__":
    main()
