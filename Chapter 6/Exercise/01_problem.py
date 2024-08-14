# Write a program to find the greatest of four numbers entered by the user.
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))
d = int(input("Enter Fourth Number: "))

if a > b:
    if c > a:
        if c < d:
            print(f"{d} is the greatest number")
        else:
            print(f"{c} is the greatest number")
    else:
        if a > d:
            print(f"{a} is the greatest number")
        else:
            print(f"{d} is the greatest number")
else:
    if b > c:
        if b > d:
            print(f"{b} is the greatest number")
        else:
            print(f"{d} is the greatest number")
    else:
        if c > d:
            print(f"{c} is the greatest number")
        else:
            print(f"{d} is the greatest number")