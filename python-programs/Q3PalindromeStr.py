"""
Write a python Program to check a if a string is Plaindrome or not
"""
def checkPalindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
str = input("Enter String: ")
if checkPalindrome(str):
    print("String is Palindrome")
else:
    print("String is not Palindrome")
