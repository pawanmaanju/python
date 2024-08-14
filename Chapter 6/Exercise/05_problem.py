# Write a program which finds out whether a given name is present in a list or not.
list1=["Pawan","Rakesh", "Mahesh","Ramesh"]
Name=input("Enter The Name : ")

if (Name.capitalize() in list1):
    print("Yes, your name is in the list.")
else:
    print("Your name is not in the list.")
    