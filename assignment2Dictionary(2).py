#2. Merge two Python dictionaries into one.
def merge_two_dicts(dict1, dict2):
    dict3 = dict1.copy()   
    dict3.update(dict2)
    return dict3

def main():
   
    n = input("Enter elements for dictionary 1 (key:value pairs separated by commas): ")
    dict1l = n.split(",")
    dict1 = {}
    for pair in dict1l:
        key, value = pair.split(":")
        dict1[key.strip()] = value.strip()
    m = input("Enter elements for dictionary 2 (key:value pairs separated by commas): ")
    dict2l = m.split(",")
    dict2 = {}
    for pair in dict2l:
        key, value = pair.split(":")
        dict2[key.strip()] = value.strip()
    dict3 = merge_two_dicts(dict1, dict2)
    print("Merged dictionary:", dict3)
if __name__ == "__main__":
    main()
 