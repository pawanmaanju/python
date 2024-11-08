"""
 Write a program to print the following star pattern:
*
**
*** for n = 3

"""
# Input the number of rows for the pattern
n = int(input("Enter the number : ")) 

# Loop to iterate through the rows, from 1 to n
for i in range(1, n+1):
    # Print i stars for each row
    print("*" * i, end="")  # Print stars without a newline at the end
    print("")  # Move to the next line after printing each row