"""
Python Program to find the factorial of a number
"""
number = int(input("Enter a number: "))

def factorial(num):
    if num == 0:
        return 1 #factorial of 0 is 1
    elif num<0:
        print("Invalid Input")
        return None
    else:
        # Initialize the `fact` variable to 1
        fact = 1
        for i in range(1,num+1):
            fact = fact * i 
        return fact
output = factorial(number)
print(f"Factorial of {number} is {output}")
