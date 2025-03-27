# Project: Binary Search
# Yeh project ek sorted list me diya gaya number dhundhne ke liye hai.

# Required Libraries:
# Is project ke liye koi additional library install karne ki zaroorat nahi hai.

def binary_search(lst, target):
    """ Diye gaye sorted list me target number dhundhne ke liye binary search ka istemal karega. """
    low = 0
    high = len(lst) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid  # Target mil gaya, index return karein
        elif lst[mid] < target:
            low = mid + 1  # Right side search karein
        else:
            high = mid - 1  # Left side search karein
    
    return -1  # Target nahi mila

if __name__ == "__main__":
    # Sorted list
    numbers = [1, 3, 5, 7, 9, 11, 13, 15]
    print("Available numbers:", numbers)
    
    target = int(input("Search karne ke liye number likhein: "))
    result = binary_search(numbers, target)
    
    if result != -1:
        print(f"Number {target} list ke index {result} par mila hai.")
    else:
        print("Number list me nahi mila.")
