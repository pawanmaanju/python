# Prompt the user to input names and corresponding marks
n1 = input("Enter Name : ")
m1 = int(input("Enter Marks : "))

n2 = input("Enter Name : ")
m2 = int(input("Enter Marks : "))

n3 = input("Enter Name : ")
m3 = int(input("Enter Marks : "))

n4 = input("Enter Name : ")
m4 = int(input("Enter Marks : "))

n5 = input("Enter Name : ")
m5 = int(input("Enter Marks : "))

# Create a dictionary to store names and their corresponding marks
marks = {
    n1: m1,
    n2: m2,
    n3: m3,
    n4: m4,
    n5: m5,
}

# Print the dictionary
print(marks)