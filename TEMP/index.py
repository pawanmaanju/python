
def print_user_details(full_name, age, number):
    print("Your Name Is: " + full_name)
    print("Your Age Is: " + str(age))  # Convert age to string
    print("Your Number Is: " + str(number))  # Convert number to string
    print()  # Adding a blank line for better output formatting


# Get inputs for full name, age, and phone number, and pass them to the print_user_details function
age = int(input("Enter Your Age: "))  # Convert age to integer
phone_number = int(input("Enter Your Number: "))  # Convert phone number to integer

# Call the function to display user details

while True:
    full_name = input("Enter Your Full Name: ")
    if(full_name==full_name.isalpha()):
        print("Write Name")
    else:
        print("Wrong Input Please Enter Only Name")
print_user_details(full_name, age, phone_number)