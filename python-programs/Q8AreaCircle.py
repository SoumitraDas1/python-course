PI = 3.14159 

# Function to calculate the area of a circle
def area_of_circle(radius):
    return PI * radius * radius

# Function to display the menu and handle user input
def menu():
    while True:
        print("\nMenu:")
        print("1. Find Area of a Circle")
        print("2. Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            radius = float(input("Enter the radius of the circle: "))
            if radius < 0:
                print("Radius cannot be negative. Please enter a valid radius.")
            else:
                area = area_of_circle(radius)
                print(f"The area of the circle with radius {radius} is: {area:.2f}")
        elif choice == 2:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")
if __name__ == "__main__":
# Call the menu function to start the program
    menu()
