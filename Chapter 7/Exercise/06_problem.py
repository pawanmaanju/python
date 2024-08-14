# Write a program to calculate the factorial of a given number using for loop.

# Prompt the user to enter a number
n = int(input("Enter the number : "))

# Initialize the product variable to 1 (since factorial starts with multiplication identity)
product = 1

# Loop from 1 to n (inclusive) to calculate the factorial
for i in range(1, n + 1):
    # Multiply the current value of 'product' by 'i'
    product *= i

# Print the factorial of the given number
print(f"Factorial of {n} is {product}")
print("")