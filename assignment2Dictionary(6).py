#6. Check if a value exists in a dictionary.
def main():
    n = input("Enter elements for the dictionary (key:value pairs separated by commas): ")
    dict_list = n.split(",")
    dict = {}
    for pair in dict_list:
        key, value = pair.split(":")
        dict[key.strip()] = value.strip()
    check_value = input("Enter the value to check: ")
    if check_value in dict.values():
        print(f"The value '{check_value}' exists in the dictionary.")
    else:
        print(f"The value '{check_value}' does not exist in the dictionary.")

if __name__ == "__main__":
    main()