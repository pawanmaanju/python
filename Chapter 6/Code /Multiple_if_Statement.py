# Prompt for name
b = input("Enter Your Name : ")

# Prompt for age
a = int(input("Enter Your Age : "))

# Check if age is even
if (a % 2 == 0):
    print("Even Number ")
# End of if Statement No : 1

# Classify user based on age
if a > 18:
    print(f"{b}, You are Adult")
    print("You Can Not Drive")
elif a < 0:
    print(f"{b}, Your Age input Is Wrong")
else:
    print(f"{b}, You are Minor")
    print("You Can Drive")
# End of if Statement No : 2

print("End The Processing")