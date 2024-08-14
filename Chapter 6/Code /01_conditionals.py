# Prompt the user to enter their name and store it in variable 'b'
b = input("Enter Your Name : ")

# Prompt the user to enter their age, convert it to an integer, and store it in variable 'a'
a = int(input("Enter Your Age : "))

# Check if the age entered is greater than 18
if a > 18:
    # If age is greater than 18, print that the user is an adult
    print(f"{b}, You are an Adult")
else:
    # If age is 18 or less, print that the user is a minor
    print(f"{b}, You are a Minor")

# Print a message indicating the end of the process
print("End The Processing")