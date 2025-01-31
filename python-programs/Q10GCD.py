def gcd(a, b):
    # Euclidean algorithm to find GCD
    while b != 0:
        a, b = b, a % b
    return a

def main():
    # User input
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Calculate and display the GCD
    result = gcd(num1, num2)
    print(f"The GCD of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()
