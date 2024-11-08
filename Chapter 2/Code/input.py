# INPUT () FUNCTION
print("")
print(":: INPUT () FUNCTION :: ")
print("")

# Taking two integer inputs from the user
a = int(input("Enter The First  Number : "))  # Converts the input to an integer
b = int(input("Enter The Second Number : "))  # Converts the input to an integer

# Displaying the entered numbers
print("First  Number IS : ", a)
print("Second Number IS : ", b)

# Displaying the sum of the two numbers
print("Sum IS : ", a + b)


                                #Explanation:
"""
	1.	input() Function: The input() function prompts the user to input data as a string. Since you want numbers, the int() function converts the string to an integer.
	•	a = int(input("Enter The First  Number : ")): Prompts the user for the first number and converts it to an integer.
	•	b = int(input("Enter The Second Number : ")): Prompts the user for the second number and converts it to an integer.
	2.	Displaying the Results:
	•	print("First  Number IS : ", a): Displays the first number entered by the user.
	•	print("Second Number IS : ", b): Displays the second number entered by the user.
	•	print("Sum IS : ", a + b): Displays the sum of the two numbers.
"""