#NEGATIVE SLICING

print("")
print(":: NEGATIVE SLICING :: ")
print("")
Name ="Pawan"
print(Name[0:3] )   #  P   A    W    A    N
print(Name[-4:-1] ) #  0   1    2    3    4  
print(Name[1:4] )   # -5  -4   -3   -2   -1

print(Name[:1]) # Start Empty Means Index Start with 0
print(Name[1:]) # End Empty Means Index End with -1

#SKIP VALUE

print("")
print(":: SKIP VALUE :: ")
print("")
word="Amazing"
print(word[1:6:2]) # first index from 1[m] to 6[n] then how many word skip 2[z] 
print(word[1:6])  
numbers="0123456789"
print(numbers[0:6:2])

