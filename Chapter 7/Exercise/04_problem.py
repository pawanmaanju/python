# Write a program to find whether a given number is prime or not.
# Prompt the user to enter a number to check for primality
n = int(input("Enter the number : "))

# Check if n is less than 2, as numbers less than 2 are not prime
if n < 2:
    print(f"{n} is not a prime number")
else:
    # Assume the number is prime initially
    is_prime = True
    
    # Check divisibility from 2 up to the square root of n (more efficient)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            # If n is divisible by i, it is not a prime number
            print(f"{n} is not a prime number")
            is_prime = False
            break
    
    # If no divisors were found, n is a prime number
    if is_prime:
        print(f"{n} is a prime number")