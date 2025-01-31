"""
Write a Python Program to that find out factorial of a number using recursion.
"""
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)

def main():
    # User input
    num = int(input("Enter a number: "))

    # Check if input is a non-negative integer
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        # Calculate and display the factorial
        result = factorial(num)
        print(f"The factorial of {num} is: {result}")

if __name__ == "__main__":
    main()
