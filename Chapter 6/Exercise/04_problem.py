"""Write a program to find whether a given username contains less than 10
characters or not."""
username=input("Enter Your Username : ")
if(len(username)<10):
    print("Your Username is less then 10 character ")
else:
    print("Your Username is more then 20 character")
    print("Done!")