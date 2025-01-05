# Function to perform the partitioning
def partition(arr, low, high):
    pivot = arr[high]  # Choose the rightmost element as the pivot
    i = low - 1        # Pointer for the greater element

    # Traverse through all elements and compare each with the pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap the pivot element with the greater element at i+1
    return i + 1

# Function to perform Quick Sort
def quick_sort(arr, low, high):
    if low < high:
        # pi is the partitioning index
        pi = partition(arr, low, high)

        # Recursively sort the elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Get the list of numbers from the user
user_input = input("Enter numbers separated by spaces: ")
# Convert the string input to a list of integers
arr = list(map(int, user_input.split()))

# Print the unsorted list
print("Unsorted list:", arr)
# Sort the list using Quick Sort
quick_sort(arr, 0, len(arr) - 1)
# Print the sorted list
print("Sorted list:", arr)
