def avg():
    while True:
        # Taking inputs from the user
        a = input("Enter your first number (or press Enter to stop): ")
        if a == '':  # If input is blank, stop the loop
            print("Thank You!")
            break
            
        b = input("Enter your second number (or press Enter to stop): ")
        if b == '':
            print("Thank You!")
            break

        c = input("Enter your third number (or press Enter to stop): ")
        if c == '':
            print("Thank You!")
            break

        # Convert inputs to integers and calculate the average
        avg_value = (int(a) + int(b) + int(c)) / 3
        print("The average is:", avg_value)

# Run the function
avg()







# if you not understand then you can watch this video

# https://youtu.be/UrsmFxEIp5k?t=17454