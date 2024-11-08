# Prompt the user to enter the start number and convert it to an integer
a = int(input("Enter the Start Number: "))

# Prompt the user to enter the end number and convert it to an integer
b = int(input("Enter the End Number: "))

# Loop until the start number is greater than the end number
while a < b + 1:
    # Print the current value of a
    print(a)
    # Increment the value of a by 1
    a += 1 		# i = i+1 

						#Output
"""
Enter the Start number : 1 
Enter the End number : 6

1     
2
3
4
5
6
"""
# 					proccess
"""
condition 1 : if a(1)<6 then execute the code
condition 2 : then print(a)
condition 3 : after the print go to first line of loop 
condition 4 : then a = a+1 increase the value of a 
condition 5 : new vlaue of a is 2
condition 6 : if a(2)<6 then execute the code
"""

#      Read More
"""
                            How the code works:
	1.  Input: The program first asks the user to enter two numbers: the start number (a) and the end number (b).
	2.	Conversion: The input values are read as strings and then converted to integers using the int() function.
	3.	While Loop: The while loop starts with the condition a < b + 1. This means the loop will continue to execute as long as the value of a is less than or equal to b.
	4.	Printing and Incrementing:
	•	Inside the loop, the current value of a is printed.
	•	The value of a is then incremented by 1 (a += 1).
	5.	Loop Execution: The loop repeats, printing the next number each time, until a exceeds b. At this point, the condition a < b + 1 becomes false, and the loop terminates.

Example:

If the user inputs 5 for the start number and 10 for the end number:

	•	The first iteration prints 5, then a is incremented to 6.
	•	The second iteration prints 6, then a is incremented to 7.
	•	This continues until a reaches 11, at which point the condition a < b + 1 (i.e., 11 < 11) is false, and the loop stops.

The output will be:
5
6
7
8
9
10
"""




