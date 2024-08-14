'''
Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user.
'''
Marks1=int(input("Enter First Subject Marks : "))
Marks2=int(input("Enter Second Subject Marks : "))
Marks3=int(input("Enter Third Subject Marks : "))

total_percentage  = ((100)*(Marks1+Marks2+Marks3)/300)
print("\nYour Total Marks Is : ",total_percentage)
if(total_percentage>=40 and Marks1>=33 and Marks2>=33 and Marks3>=33):
    print("\nYou Are Passed")
else:
    print("\nYou Are Failed , Better Try Next Time!")

