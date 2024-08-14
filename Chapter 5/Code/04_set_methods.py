# Create a set with duplicate and unique values
s = {33, 44, 55, 0, 22, 0, 33, 44, 0, 55, "pawan"}
print(s)  # Output: {0, 33, 44, 55, 22, 'pawan'}

# Add a new element to the set
s.add(77)
print(s)  # Output: {0, 33, 44, 55, 22, 'pawan', 77}

# Create two sets
s1 = {1, 2, 3}
s2 = {2, 3, 4}

# Add an element to s1
s1.add(5)  # s1 becomes {1, 2, 3, 5}

# Remove an element from s1
s1.remove(2)  # s1 becomes {1, 3, 5}

# Discard an element from s1 (no error if element does not exist)
s1.discard(10)  # s1 remains {1, 3, 5}

# Pop an arbitrary element from s1
element = s1.pop()  # Removes and returns an arbitrary element, s1 becomes {3, 5} or similar
print("Popped element:", element)

# Clear all elements from s1
s1.clear()  # s1 becomes set()

# Copy s1 to s_copy
s1 = {1, 2, 3}
s_copy = s1.copy()  # s_copy is {1, 2, 3}

# Union of s1 and s2
s_union = s1.union(s2)  # s_union becomes {1, 2, 3, 4}

# Intersection of s1 and s2
s_intersection = s1.intersection(s2)  # s_intersection becomes {2, 3}

# Difference between s1 and s2
s_difference = s1.difference(s2)  # s_difference becomes {1}

# Symmetric difference between s1 and s2
s_sym_diff = s1.symmetric_difference(s2)  # s_sym_diff becomes {1, 4}

# Output results
print("s1:", s1)
print("s2:", s2)
print("s_copy:", s_copy)
print("s_union:", s_union)
print("s_intersection:", s_intersection)
print("s_difference:", s_difference)
print("symmetric_difference:", s_sym_diff)