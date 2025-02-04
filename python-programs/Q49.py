def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Target found, return its index
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
    return -1  # Target not found

# Taking user input
arr = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))
target = int(input("Enter the number to search for: "))

# Performing binary search
result = binary_search(arr, target)

# Displaying the result
if result != -1:
    print(f"Number found at index {result}.")
else:
    print("Number not found in the list.")