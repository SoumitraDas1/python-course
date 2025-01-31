# Function to generate first N Fibonacci numbers
def generate_fibonacci(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return []

    # Initialize the first two Fibonacci numbers
    fibonacci_series = [0, 1]

    # Generate the series up to N terms
    while len(fibonacci_series) < n:
        next_number = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_number)

    return fibonacci_series

# User input for N
N = int(input("Enter the number of Fibonacci numbers to generate: "))

# Call the function and display the result
fibonacci_numbers = generate_fibonacci(N)
print("First", N, "Fibonacci numbers:", fibonacci_numbers)