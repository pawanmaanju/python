# Function to greet the user based on their name
def greet_user(name):
    print(name + " Good Day")

# Get user input for the name and greet them
user_name = input("Enter Your Name: ")
greet_user(user_name)


"""
                    INPUT

Enter Your Name: Pawan

                    OUTPUT

Pawan Good Day
"""

# Function to print the details of the user
def print_user_details(name, age, number):
    print("Your Name Is: " + name)
    print("Your Age Is: " + str(age))  # Convert age to string
    print("Your Number Is: " + str(number))  # Convert number to string
    print()  # Adding a blank line for better output formatting

# Get inputs for name, age, and number, and pass them to the print_user_details function
full_name = input("Enter Your Full Name: ")          
age = int(input("Enter Your Age: "))  # Convert age to integer
phone_number = int(input("Enter Your Number: "))  # Convert number to integer

# Call the function to display user details
print_user_details(full_name, age, phone_number)


"""
                    INPUT

Enter Your Full Name: Pawan Bishnoi
Enter Your Age: 20
Enter Your Number: 9876543210

                    OUTPUT
Pawan Good Day
Your Name Is: Pawan Bishnoi
Your Age Is: 20
Your Number Is: 9876543210
"""
