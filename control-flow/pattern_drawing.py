size = int(input("Enter the size of the pattern: "))

# Check for positive integer input
if size <= 0:
    print("Error: Please enter a positive integer.")
else:
    # Outer loop for rows
    for i in range(size):
        # Inner loop for columns
        for j in range(size):
            print("*", end="")  # Print asterisk without newline
        print()  # Print newline after each row
