#10. Check if all items in the tuple are the same 
if __name__ == "__main__":
    try:
        n = input("Enter a tuple of elements separated by commas: ")
        tuple = tuple(map(str.strip, n.split(',')))
        result = all(item == tuple[0] for item in tuple)
        if result:
            print("All items in the tuple are the same.")
        else:
            print("Not all items in the tuple are the same.")
    except ValueError:
        print("Invalid input.")
