"""A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams.
"""

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message=input("Enter A Comment : ")
if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This Is Spam Comment")
else:
    print("This Not Spam Comment")