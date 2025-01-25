# Python
## Designed by: *Guido Van Russom*
### First appeared: 20 February 1991
- Genral Purpose
- Easy to Learn
- Object Oriented
- Has high level data structures
- Dynamically typed
- Scripting Language
- Versatile Domains(Web Development, Data Science, Machine Learning etc)
- **Interpreter**

### Python syntax
```python
# Print the classic "Hello World" message to the console, showcasing a simple output operation.
print('Hello World')
# Print the result of the arithmetic operation 1 + 2, demonstrating basic math and the `print` function.
print(1+2)
# Assign a string value to the variable `greet`. This demonstrates variable initialization and string handling.
greet = "Welcome To our Course"
# Check if the value of the `greet` variable matches the string "Good Morning". Demonstrates an `if` statement for conditional logic.
if greet=="Good Morning":
    # If the condition is true, this line executes and prints "Good Morning" to the console.
    print("Good Morning")
else:
    # If the condition is false, this line executes and prints "Learn and Contribute" to the console.
    print("Learn and Contribute")
```

- Output

```
Hello World
3
Learn and Contribute
````

> [!Note]
> # Indenation in Python
> Indentation in Python refers to the **spaces or tabs** at the beginning of a code line. Unlike many programming languages that use braces {} or other delimiters to define code blocks, Python uses indentation to indicate a block of code. This makes Python code more readable and visually structured.
> - It is a part of the syntax
> - Indentation is not optional in Python
> - Improper indentation leads to a **IndentationError**
> - Each nested block increases the indentation level.
> - Use the **same number of spaces (or tabs)** for all lines in a block.


- ### Atoms
    - Atoms are the smallest units of code that cannot be broken down further.


- ### *Identifiers:* 
    - Identifiers are the names used to identify variables, functions, classes, modules, or other objects in Python.
    - **Rules** for Naming Identifiers:
        1. Can only contain **letters** (A-Z, a-z), **digits** (0-9), and **underscores** (_).
        2. **Must start with** a **letter or underscore** (_), not a digit.
        3. Cannot use Python keywords or built-in function names.
        4. Case-sensitive (Name and name are different).

- ### *Literals:*
    - They are fixed values assigned to variables in the program.
        ```python
        # Integer literal
        num = 42  # 42 A whole number
        # Float literal
        x = 5.1454  # 3.15 A decimal number
        # String literal
        name = "ChatGPT"  # A sequence of characters
        # Complex literal
        complex_num = 2 + 3j  # A complex number with a real and imaginary part
        # None literal
        value = None  # Represents the absence of a value or null
        # Multiline string literal
        multiline_text = """This is a
        multiline string."""
- ### *Constants:*
    - Constants are fixed, unmodifiable values.

## Keywords
- Keywords are reserved words in Python that have predefined meanings and cannot be used as identifiers.
    - Case Sensitive
    - **35 Keywords**
    - ```python
        #Use keyword module to list all keywords
        import keyword
        print(keyword.kwlist)
    - ```
        """
        ['False', 'None', 'True', 'and', 'as', 'assert', 'async',
         'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 
         'else', 'except', 'finally', 'for', 'from', 'global', 'if', 
         'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
         'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
        """
    
<details open>
<summary>Course Outline</summary>
<h2>Python Programming: Course Outline</h2>
<ol>
    <li><strong>Understanding Data Types</strong>: The building blocks of Python.</li>
    <li><strong>Mastering Operators</strong>: Perform calculations and logical operations.</li>
    <li><strong>Input and Output Handling</strong>: Interacting with users and displaying results.</li>
    <li><strong>Conditional Statements and Branching</strong>: Decision-making in Python.</li>
    <li><strong>Looping Constructs</strong>: Repeating tasks efficiently.</li>
    <li><strong>Functions</strong>: Modularize and reuse code effectively.</li>
    <li><strong>Recursion</strong>: The art of self-referential functions.</li>
    <li><strong>Classes, Objects, and Methods</strong>: Exploring the world of Object-Oriented Programming.</li>
    <li><strong>Data Structures and Algorithms</strong>: Organize and manipulate data like a pro.</li>
    <li><strong>Searching and Sorting Techniques</strong>: Optimizing data retrieval and organization.</li>
</ol>
</details>

## Basic Python Programs
1. **Check if a number is prime or not** *
2. **Find the factorial of a number** *
3. **Check if a string is a palindrome** * 
4. **Write a Python Program to generate first 'N' *Fibonacci Series*/numbers** * 
5. Sum of natural numbers  
6. Armstrong number  
7. Reverse a string  
8. **Write  a menu driven program using user defined functions to find Area of a circle** *
9. Generate Multiplication Table  
10. **Calculate GCD of two numbers**  *
11. Count the occurrence of a character in a string  
12. Convert temperature from Celsius to Fahrenheit  
13. Check if a year is a leap year  
14. Find the largest number in a list  
15. Sort a list of numbers  
16. Generate a random number  
17. Solve quadratic equations  
18. Count vowels and consonants in a string  
19. **Write  a menu driven program using user defined functions to Calculate the area of a rectangle/square** *
20. Check if a number is an even or odd number
21. Generate a histogram from a list  
22. Check if a number is a perfect number  
23. Calculate the LCM of two numbers  
24. Solve a basic mathematical expression (e.g., arithmetic operations)  
25. Remove vowels from a string  
26. Check if a string is a valid email  
27. Check if a number is a palindrome  
28. Create a simple calculator with basic operations  
29. Find the sum of digits of a number  
30. Implement a simple password validator  
31. Count the number of elements greater than a given value in a list  
32. Check if a number is a power of 2  
33. Convert binary to decimal and vice versa  
34. Generate combinations of a given length  
35. Create a simple to-do list  
36. Calculate the area of a parallelogram  
37. Count the number of special characters in a string  
38. Check if a list contains duplicate elements
39. Remove a string from a list in Python.
40. Check if a string appears in another string from a list in Python.
41. **Write a Python program to perform `Insertion sort` of an array/list.** *
42. **Write a Python program to perform `Selection sort` of an array/list.** *
43. **Write a Python program to perform `Bubble sort` of an array/list.** * 
44. **Write a python program that implements *Stack Operation***  *
45. **Write a python program that implements *Queue Operation***  *
46. **Implement *Queue* using *List*** *
47. **Write a python program to implement a *Circular Queue*** * 
48. **Write a program to print following pattern in Python** *
```
*
**
***
****
*****
```
49. **Write a Python Code to perform `Binary Search` Technique.** *
50. **Write a Python Code to Perform  `Linear Srarch` Technique**. *
51. **Write a  Python Program to that find out factorial of a number using recursion.** *
52. **Write a Python Program Using recursion to generate ten odd numbers.** *
53. **Write a Python Program to find the sum of series:** *
$$
S = \frac{1}{1!} - \frac{2}{2!} + \frac{3}{3!} - \frac{4}{4!} +... \frac{n}{n!} 
$$
54. **Write a Python Program to add two Matrix** *
55. WAP to calculate total marks, percentage and grade of a student. Marks obtained in each of
the three subjects are to be input by the user. Assign grades according to the following
criteria :
    ```
    Grade A: Percentage >=80
    Grade B: Percentage>=70 and <80
    Grade C: Percentage>=60 and <70
    Grade D: Percentage>=40 and <60 
    Grade E: Percentage<40 
    ```
56. Write a menu driven program to convert the given temperature from Fahrenheit to Celsius and vice versa depending upon users choice. 


## Intermediate Python Programs (Level 2)
1. Evaluate the prefix expression `*+23+54`.  
2. Evaluate the postfix expression `23+54+*`.  
3. Convert infix to postfix for `((3 + 4) * (5 - 2))`.  
4. Convert infix to prefix for `((3 + 4) * (5 - 2))`.  
5. Evaluate the prefix expression `+ * 5 3 - 8 2`.  
6. Evaluate the postfix expression `23 45 6 * +`.  
7. Identify errors in prefix expression `*+23-54`.  
8. Evaluate the postfix expression `5 1 2 + 4 * + 3 -`.  
9. Validate prefix expression `* + 2 3 5`.  
10. Validate postfix expression `23 45 + *`.

