a = (22, 33, 44, "Rohan", "Mahesh", False, 22.44, 44)

# Print the tuple
print(a)

# Count the occurrences of 44 in the tuple
print(a.count(44))

# Find the index of the first occurrence of 22.44
print(a.index(22.44))

# Access the first element
print(a[0])

# Slice the tuple from index 1 to 3
print(a[1:4])

# Concatenate t1 and t2
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print(t3)

# Repeat the tuple 3 times
print(a * 3)

# Check if 2 is in the tuple
is_in = 2 in a
print(is_in)

# Check if 5 is not in the tuple
is_not_in = 5 not in a
print(is_not_in)

# Get the length of the tuple
print(len(a))

# Creating another tuple with only numeric values
b = (22, 66, 44, 77, 44, 33, 22, 44)

# Get the minimum value in the tuple
print(min(b))

# Get the maximum value in the tuple
print(max(b))

# Get the sum of all elements in the tuple
print(sum(b))

# Convert the tuple 'a' to a list
print(list(a))