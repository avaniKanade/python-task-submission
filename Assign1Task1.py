# Ask the user to enter the first number
first_number = input("Enter the first number: ")
# Ask the user to enter the second number
second_number = input("Enter the second number: ")

# Convert the input to numbers (floats allow decimals too)
first_number = float(first_number)
second_number = float(second_number)

# Do the math operations
add = first_number + second_number
subtract = first_number - second_number
multiply = first_number * second_number

# Handle division carefully (don't divide by zero!)
if second_number != 0:
    divide = first_number / second_number
else:
    divide = "Cannot divide by zero"

# Show the results
print("\nHere are the results:")
print("Addition:", add)
print("Subtraction:", subtract)
print("Multiplication:", multiply)
print("Division:",divide)