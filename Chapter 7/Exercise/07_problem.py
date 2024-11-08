'''
Write a program to print the following star pattern.
for n = 3
  *
 ***
***** 
For n = 5
    *
   ***
  *****
 ********
**********
'''
# Input the number of rows for the pattern
n = int(input("Enter the number : ")) 

# Loop to iterate through the rows, from 1 to n
for i in range(1, n+1):
    # Print spaces to align the stars, based on the current row
    print(" " * (n - i), end="")
    
    # Print the stars, the number of stars in each row follows the pattern (2*i - 1)
    print("*" * (2 * i - 1), end="")
    
    # Move to the next line after printing each row
    print("")



                        # Explanation
"""
	1.	n is the number of rows for the star pattern. It is taken from user input.
	2.	The outer loop runs from 1 to n, where i represents the current row.
	3.	For each row:
	•	The number of spaces printed is (n - i). This aligns the stars centrally.
	•	The number of stars printed in each row is (2 * i - 1). This creates the increasing star pattern in odd numbers (1, 3, 5, …).
	4.	After printing each row, the print("") moves the cursor to the next line.

For example:

	•	If n = 3, the output is:

  *
 ***
*****


	If n = 5, the output is:

    *
   ***
  *****
 *******
*********

"""