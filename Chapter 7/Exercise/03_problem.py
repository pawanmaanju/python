# Attempt problem 1 using while loop.
# Prompt the user to enter a number for which the multiplication table will be printed
n = int(input("Enter the number : "))

# Initialize the counter variable 'i' to 1
i = 1

# Use a while loop to iterate as long as 'i' is less than 11
while i < 11:
    # Print the multiplication expression and its result in a formatted way
    print(f"{n} X {i} = {n*i}")
    
    # Increment the counter variable 'i' by 1
    i += 1
    