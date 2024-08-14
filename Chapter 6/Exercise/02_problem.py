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

    print("\nYou Are Pass")
else:
    print("\nYou Are Fail Better Try Next Time!")

if(Marks1<=40):
    print("\nYou Are Fail In Subject 1 ")
    print("\nYour Marks : ",Marks1)
else:
    print("\nYou Are Pass In Subject 1 ")
    print("\nYour Marks : ",Marks1)

if(Marks2<=40):
     print("\nYou Are Fail In Subject 2 ")
     print("\nYour Marks : ",Marks2)
else:
    print("\nYou Are Pass In Subject 2 ")
    print("\nYour Marks : ",Marks2)

if(Marks3<=40):
     print("\nYou Are Fail In Subject 3 ")
     print("\nYour Marks : ",Marks3)
else:
    print("\nYou Are Pass In Subject 3 ")
    print("\nYour Marks : ",Marks3)


     



