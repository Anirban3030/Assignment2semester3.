import ast

input_data = input("Enter tuples of format (x, y), separated by commas: ")

tuple_strings = input_data.split(',')

data = []
for tuple_str in tuple_strings:
    try:
        t = ast.literal_eval(tuple_str)
        if isinstance(t, tuple) and len(t) == 2:
            data.append(t)
        else:
            print("Invalid tuple:", tuple_str)
    except (ValueError, SyntaxError):
        print("Invalid input:", tuple_str)

print("Data:", data)
sorted_data = sorted(data, key=lambda x: x[1])

print(sorted_data)
