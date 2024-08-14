# Prompt the user to enter their name and store it in variable 'b'
b = input("Enter Your Name : ")

# Prompt the user to enter their age, convert it to an integer, and store it in variable 'a'
a = int(input("Enter Your Age : "))

# if elif else ladder to classify user based on age
if a > 18:
    # If age is greater than 18, print that the user is an adult
    print(f"{b}, You are an Adult")
elif a < 0:
    # If age is less than 0, print an error message indicating wrong age input
    print(f"{b}, Your Age Input Is Wrong")
else:
    # If age is 18 or less (but not negative), print that the user is a minor
    print(f"{b}, You are a Minor")

# Print a message indicating the end of the processing
print("End The Processing")