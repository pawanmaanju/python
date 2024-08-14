# Write a program to print multiplication table of a given number using for loop.
# Prompt the user to enter a number for which the multiplication table will be printed
n = int(input("Enter the number : "))

# This commented-out code is an alternative method for printing the multiplication table
# It uses a different approach that generates multiples of the number directly
# for i in range(n, n*11, n):
#     print(i)

# Loop through numbers 1 to 10 to generate the multiplication table
for i in range(1, 11):
    # Print the multiplication expression and its result in a formatted way
    print(f"{n} X {i} = {n*i}")