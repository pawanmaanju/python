# Write a program to greet all the person names stored in a list ‘l’ and which starts with S.

# List of names
l = ["Pawan", "Ramesh", "Sohan", "Sachin"]

# Print the list of names (optional, used to display the list before processing)
print(l)

# Loop through each name in the list
for name in l:
    # Check if the current name starts with the letter "S"
    if name.startswith("S"):
        # Greet the person with a formatted string
        print(f"Hello {name}")