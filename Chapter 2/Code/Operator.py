# Arithmetic Operator
print("")
print(":: Arithmetic Operator :: ")
print("")

a  = 10
b  = 20
print(a+b)


#Assignment Operator 
print("")
print(":: Assignment Operator :: ")
print("")

a= 20
b= 30

b+=a # Increment the value by a and then assign it to b
print(b)
b-=a # Decrement the value by a and then assign it to b
print(b)

#Comparison Operator
print("")
print(":: Comparison Operator :: ")
print("")
a=10
b=20
c=10
print("a is equal to b : ",a==b)
print("a is greater then b : ",a>b)
print("a is less then b : ",a<b)
print("a is greater  then or equal to  b : ",a>=b)
print("a is greater then or equal to b : ",a>=b)
print("a is greater then or equal to c : ",a>=c)
print("a is not equal to b : ",a!=b)

#logical Operator 
print("")
print(":: logical Operator ::")
print("")
print(": OR :")

e= True or False
print(" { True or False } : ",e)
a = 20
b=30
c=20
d = a<b or a>b # any one is true output is true
print(" { a<b or a>b } : ",d)
d = a<=c or a>=c
print(" { a<=c or a>=c } : ",d)
d = a>b or c>b # all false output false 
print(" { a>b or c>b } : ",d)

print(": AND :")

e= True and False
print(" { True and False } : ",e)
a = 20
b=30
c=20
d = a<b and a>b # any one is true output is true
print(" { a<b and a>b } : ",d)
d = a<=c and a>=c
print(" { a<=c and a>=c } : ",d)
d = a>b and c>b # all false output false 
print(" { a>b and c>b } : ",d)
print(not(True)) # True to false and false to true : Not :


