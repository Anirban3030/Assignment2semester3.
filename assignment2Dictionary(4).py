#4. Create a dictionary by extracting the keys from a given dictionary. 
def main():
   
    n = input("Enter elements of the dictionary (key:value pairs separated by commas): ")
    original_dict_l = n.split(",")

    
    original_dict = {}
    for pair in original_dict_l:
        key, value = pair.split(":")
        original_dict[key.strip()] = value.strip()

    
    new_dict = {}
    for key in original_dict:
        m = input(f"Enter new value for key '{key}': ")
        new_dict[key] = m

    print("New dictionary :", new_dict)

if __name__ == "__main__":
    main()
