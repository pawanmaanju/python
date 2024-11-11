# Function to greet the user based on their name
def greet_user(user_name, ending): # function With Argment {def greet_user Is Function & ending is argument }
    print("Good Day, " + user_name)
    print(ending)
    return "Done" 


# Get user input for the name and greet them
user_name = input("Enter Your Name: ")
# Calling greet_user with the required arguments
greet_user(user_name, "Welcome!")
# print(user_name)


"""
                    INPUT

Enter Your Name: Pawan

                    OUTPUT

Good Day, Pawan
Welcome!
Pawan
"""


# Function to print the details of the user
def print_user_details(full_name, age, number):
    print("Your Name Is: " + full_name)
    print("Your Age Is: " + str(age))  # Convert age to string
    print("Your Number Is: " + str(number))  # Convert number to string
    print()  # Adding a blank line for better output formatting


# Get inputs for full name, age, and phone number, and pass them to the print_user_details function
full_name = input("Enter Your Full Name: ")
age = int(input("Enter Your Age: "))  # Convert age to integer
phone_number = int(input("Enter Your Number: "))  # Convert phone number to integer

# Call the function to display user details
print_user_details(full_name, age, phone_number)


"""
                    INPUT

Enter Your Full Name: Pawan Bishnoi
Enter Your Age: 20
Enter Your Number: 9876543210

                    OUTPUT
Good Day, Pawan
Welcome!
Pawan
Your Name Is: Pawan Bishnoi
Your Age Is: 20
Your Number Is: 9876543210
"""


# if you not understand then you can watch this video

# https://youtu.be/UrsmFxEIp5k?t=17454