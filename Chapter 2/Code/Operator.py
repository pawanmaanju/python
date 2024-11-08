# Arithmetic Operator
print("")
print(":: Arithmetic Operator :: ")
print("")

a = 10
b = 20
print(a + b)

	
                            #	Explanation:
"""
     + is an arithmetic operator used to add two numbers. 
     Here, the sum of a and b (10 + 20) is printed, resulting in 30.
"""
# Assignment Operator
print("")
print(":: Assignment Operator :: ")
print("")

a = 20
b = 30

b += a  # Increment b by a (b = b + a)
print(b)  # Output: 50

b -= a  # Decrement b by a (b = b - a)
print(b)  # Output: 30


                            #	Explanation:
"""
	•	+= adds the value of a to b, and -=, subtracts the value of a from b.
	•	Initially, b is incremented by a (30 + 20 = 50), and then it’s decremented by a (50 - 20 = 30).
"""


# Comparison Operator
print("")
print(":: Comparison Operator :: ")
print("")

a = 10
b = 20
c = 10

print("a is equal to b : ", a == b)
print("a is greater than b : ", a > b)
print("a is less than b : ", a < b)
print("a is greater than or equal to b : ", a >= b)
print("a is greater than or equal to c : ", a >= c)
print("a is not equal to b : ", a != b)

                            #	Explanation:
"""
	•	Comparison operators like ==, >, <, >=, and != are used to compare values.
	•	a == b checks if a is equal to b (False), a < b checks if a is less than b (True), etc.
"""


# Logical Operator
print("")
print(":: Logical Operator ::")
print("")
print(": OR :")

e = True or False
print(" { True or False } : ", e)

a = 20
b = 30
c = 20

d = a < b or a > b
print(" { a<b or a>b } : ", d)  # True, because one condition is True

d = a <= c or a >= c
print(" { a<=c or a>=c } : ", d)  # True, both are True

d = a > b or c > b
print(" { a>b or c>b } : ", d)  # False, both conditions are False

print(": AND :")

e = True and False
print(" { True and False } : ", e)  # False, because both need to be True

d = a < b and a > b
print(" { a<b and a>b } : ", d)  # False, one condition is False

d = a <= c and a >= c
print(" { a<=c and a>=c } : ", d)  # True, both conditions are True

d = a > b and c > b
print(" { a>b and c>b } : ", d)  # False, both conditions are False

print(not(True))  # Inverts True to False

                            #	Explanation:
"""
	•	Explanation:
	•	or: The result is True if at least one condition is true.
	•	and: The result is True only if both conditions are true.
	•	not: Inverts the boolean value (True becomes False, and vice versa).

Summary of Outputs:

	•	Arithmetic Operator Output: 30
	•	Assignment Operator Output:
	•	50 (after b += a)
	•	30 (after b -= a)
	•	Comparison Operator Output:
	•	False for a == b
	•	True for a < b, a >= c, etc.
	•	Logical Operator Output:
	•	Various combinations of True and False based on the conditions.
"""