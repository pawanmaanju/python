# Write a program to fill in a letter template given below with name and date.
from datetime import datetime

# Get the current date
current_date = datetime.now().date()
date=str(current_date)

letter = '''Dear <|Name|>,
         You are selected!
                     <|Date|>
'''
user=input("Enter Your Name : ")
print(letter.replace("<|Name|>",user).replace("<|Date|>",date))