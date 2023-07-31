#6. Copy specific elements from one tuple to a new tuple. 
input_values = input("Enter values separated by spaces: ").split()
original_tuple = tuple(input_values)
start_index = int(input("Enter the start index: "))
end_index = int(input("Enter the end index (exclusive): "))

if start_index < 0 or end_index > len(original_tuple) or start_index >= end_index:
    print("Invalid input for slicing.")
else:
    new_tuple = original_tuple[start_index:end_index]
   
    print("New tuple:", new_tuple)
