def is_palindrome(number):
    original_number = number
    reverse_number = 0

    while number > 0:
        digit = number % 10  # Extract the last digit
        reverse_number = reverse_number * 10 + digit  # Append the digit to the reverse number
        number = number // 10  # Remove the last digit

    return reverse_number == original_number

def main():
    # User input
    num = int(input("Enter a number: "))

    # Check if it's a palindrome and display the result
    if is_palindrome(num):
        print(f"{num} is a palindrome!")
    else:
        print(f"{num} is not a palindrome.")

if __name__ == "__main__":
    main()

