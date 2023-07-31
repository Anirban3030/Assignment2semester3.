#7. Modify the tuple. 
input_values = input("Enter values separated by spaces: ").split()
original_tuple = tuple(input_values)
modified_list = list(original_tuple)
index_to_modify = int(input("Enter the index to modify: ")) 
if 0 <= index_to_modify < len(modified_list):
    new_value = input("Enter the new value: ")
    modified_list[index_to_modify] = new_value

    
    modified_tuple = tuple(modified_list)
    print("Modified tuple:", modified_tuple)
else:
    print("Invalid index. The index should be between 0 and", len(modified_list) - 1)
