# Q Write a program to accept marks of 6 students and display them in a sorted manner.

# Initialize an empty list to store marks Numbers
Marks = []

# Prompt the user to enter the mirst marks Number and append it to the list
m1 = int(input("Enter Marks here: "))
Marks.append(m1)

# Prompt the user to enter the second marks Number and append it to the list
m2 = int(input("Enter Marks here: "))
Marks.append(m2)

# Prompt the user to enter the third marks Number and append it to the list
m3 = int(input("Enter Marks here: "))
Marks.append(m3)

# Prompt the user to enter the mourth marks Number and append it to the list
m4 = int(input("Enter Marks here: "))
Marks.append(m4)

# Prompt the user to enter the mimth marks Number and append it to the list
m5 = int(input("Enter Marks here: "))
Marks.append(m5)

# Prompt the user to enter the sixth marks Number and append it to the list
m6 = int(input("Enter Marks here: "))
Marks.append(m6)


Marks.sort()
# Print the list om Marks entered by the user
print("\t: Your Marks : \n", Marks)