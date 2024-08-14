# Write a program to find the greatest of four numbers entered by the user.
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))
d = int(input("Enter Fourth Number: "))

if(a>b and a>c and a<d):
    print(f"{a} Is Greatest Number")
elif(b>a and b>c and b>d):
    print(f"{b} Is Greatest Number")
elif(c>a and c>b and c>d):
    print(f"{c} Is Greatest Number")
else:
    print(f"{d} Is Greatest Number")