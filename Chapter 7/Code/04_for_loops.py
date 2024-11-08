# without user input
i = 0  # Initialize i to 0
for i in range(4):  # Loop over a range of numbers from 0 to 3 (range(4) produces 0, 1, 2, 3)
    print(i)  # Print the value of i in each iteration

# with user input
a = int(input("Enter the Starting number : "))  # Take input from the user for the starting number, convert it to an integer, and store it in 'a'
b = int(input("Enter the End number : "))  # Take input from the user for the ending number, convert it to an integer, and store it in 'b'

# Loop over the range starting from 'a' to 'b' (inclusive of 'b', as b+1 is given)
for i in range(a, b + 1):
    print(i)  # Print the value of i in each iteration