# Create a dictionary with mixed key types
marks = {
    "Pawan": 100,
    "Mahesh": 70,
    "Rakesh": 50,
    30: "Ramesh" 
}

# Print all key-value pairs in the dictionary as a view object
print(marks.items())

# Print len of dictionary
print(len(marks))

# Print all keys in the dictionary as a view object
print(marks.keys())

# Print all values in the dictionary as a view object
print(marks.values())

# Get the value for the key "Pawan" get print None 
print(marks.get("Pawan"))

print(marks['Pawan']) # return an error

# Attempt to get the value for the key 'other'; return 'default' if the key does not exist
print(marks.get('other', 'default'))

# Update the value for 'Rakesh' with the new value; Note: the last value ('Rakesh': 51) will be used
marks.update({'Rakesh': 50, 'Rakesh': 51})
print(marks)

# Remove and return the value for the key 'Mahesh'
print(marks.pop('Mahesh'))

# Create a shallow copy of the dictionary
print(marks.copy())

# Set default value for the key 'Pawan' and return its value
print(marks.setdefault('Pawan', 100))

# Uncommenting this line will cause an error; 'popitem' is a method of dictionaries, not 'd'
print(marks.popitem())

# Clear all key-value pairs from the dictionary
marks.clear()

# Print the dictionary after clearing it
print(marks)


'''
    1.	marks.items(): Returns a view object displaying a list of dictionary’s key-value tuple pairs.
	2.	marks.keys(): Returns a view object displaying a list of all the keys in the dictionary.
	3.	marks.values(): Returns a view object displaying a list of all the values in the dictionary.
	4.	marks.get("Pawan"): Retrieves the value associated with the key "Pawan". If the key does not exist, it returns None.
	5.	marks.get('other', 'default'): Retrieves the value for the key 'other' if it exists; otherwise, it returns 'default'.
	6.	marks.update({'Rakesh': 50, 'Rakesh': 51}): Updates the dictionary with new key-value pairs. If a key already exists, its value is updated. The last value provided for a key is used.
	7.	marks.pop('Mahesh'): Removes the key 'Mahesh' from the dictionary and returns its value. If the key does not exist, it raises a KeyError.
	8.	marks.copy(): Creates a shallow copy of the dictionary.
	9.	marks.setdefault('Pawan', 100): Returns the value for the key 'Pawan'. If the key does not exist, it sets it to 100 and then returns 100.
	10.	marks.clear(): Removes all items from the dictionary.

'''