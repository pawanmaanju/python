# def gd(age):
#     print(age+" Good Day")

# gd(input("Enter Your Name : "))

def details(Name, age, Number):
    print("Your Name Is : " + Name)
    print("Your Age Is : " + str(age))  # Convert age to string
    print("Your Number Is : " + str(Number))  # Convert Number to string
    print
# Get inputs and pass them to the details function
Name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))  # Convert age to integer
Number = int(input("Enter Your Number: "))  # Convert Number to integer

details(Name, age, Number)

