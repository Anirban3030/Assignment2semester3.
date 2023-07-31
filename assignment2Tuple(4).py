#4. Unpack the tuple into 4 variables. 
input_values = input("Enter four values separated by spaces: ").split()
while len(input_values) < 4:
    input_values = input("Enter four values separated by spaces: ").split()
try:
    value1, value2, value3, value4 = map(int, input_values)
    print("Unpacked values:")
    print("Value 1:", value1)
    print("Value 2:", value2)
    print("Value 3:", value3)
    print("Value 4:", value4)
except ValueError:
    print("Invalid input. ")
