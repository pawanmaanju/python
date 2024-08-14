# Write a program to find the sum of first n natural numbers using while loop

# Prompt the user to enter a number
n = int(input("Enter the number : "))

# Initialize the counter variable 'i' to 0
i = 0

# Initialize the sum variable to 0
sum = 0

# Use a while loop to iterate from 0 to n (inclusive)
while i <= n:
    # Add the current value of 'i' to the sum
    sum += i
    
    # Increment the counter variable 'i' by 1
    i += 1

# Print the final sum of all integers from 0 to n
print(sum)