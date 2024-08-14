# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
# Define the dictionary with translations
tra = {
    "Book": "Kitaab",
    "Chair": "Kursi",
    "help": "Madad",
    "Cat": "Billi",
}

# Prompt the user to enter a word
user = input("Enter the word you want meaning of: ")

# Retrieve and print the meaning if the word is in the dictionary
print(tra[user])
