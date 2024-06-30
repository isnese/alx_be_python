size = int(input("Enter the size of the pattern: "))

# Check for positive integer input
if size <= 0:
    print("Error: Please enter a positive integer.")
else:
    i = 0  # Initialize loop counter
    while i < size:
        # Inner loop for columns (same as before)
        for j in range(size):
            print("*", end="")
        print()  # Newline after each row
        i += 1  # Increment loop counter
