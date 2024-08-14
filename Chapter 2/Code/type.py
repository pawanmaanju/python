# TYPE() FUNCTION
print("")
print(":: TYPE() FUNCTION :: ")
print("")

a = 30  
b =type(a) # class <int>
print(b)

a = 30.22 
b =type(a) # class <float>
print(b)

a = "31"
b= type (a) # class <str>
print(b)

a = True
b= type (a) # class <bool>
print(b)



# TYPECASTING
print("")
print(":: TYPECASTING :: ")
print("")


a = 30  
c = float(a)
b =type(c) # class <float>
print(c)
print(b)

a = 30.22 
c = str(a)
b =type(c) # class <str>
print(c)
print(b)

a = "31"
c = int(a)
b= type(c) # class <int>
print(c)
print(b)


