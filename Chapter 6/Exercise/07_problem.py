# Write a program to find out whether a given post is talking about “Harry” or not.
post = input("Enter The Post : ")
if( "Harry".lower() in post.lower()):
    print("This post is talking about harry")
else:
    print("this post is not talking about harry")