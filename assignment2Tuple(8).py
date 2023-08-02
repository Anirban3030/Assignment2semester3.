# Get input from the user
data = input("Enter a tuple of tuples: ")
data = eval(data)  # Convert the input string to a tuple

# Sort the tuple of tuples by the 2nd item
sort = sorted(data, key=lambda x: x[1])

print("Sorted tuple of tuples:", sort)

