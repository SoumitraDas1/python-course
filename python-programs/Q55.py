def calculate_grade(percentage):
    if percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "E"

def main():
    # Input marks for three subjects
    subject1 = float(input("Enter marks for Subject 1: "))
    subject2 = float(input("Enter marks for Subject 2: "))
    subject3 = float(input("Enter marks for Subject 3: "))

    # Validate marks (assuming full marks for each subject is 100)
    if any(m < 0 or m > 100 for m in [subject1, subject2, subject3]):
        print("Invalid marks entered. Please enter marks between 0 and 100.")
        return

    # Calculate total marks
    total_marks = subject1 + subject2 + subject3

    # Calculate percentage
    percentage = (total_marks / 300) * 100

    # Determine grade
    grade = calculate_grade(percentage)

    # Display results
    print(f"\nTotal Marks: {total_marks:.2f}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

# Run the main program
if __name__ == "__main__":
    main()
