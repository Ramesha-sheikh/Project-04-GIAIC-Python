import random
import time
from bisect import bisect_left

# ------------------ Binary Search Project ------------------
# Yeh project teen search techniques ko implement karta hai:
# 1. Naive Search (Linear Search) - Slow but simple
# 2. Recursive Binary Search - Fast but requires sorted input
# 3. Built-in Bisect Search - Optimized binary search using Python's bisect module
# Is project mein performance testing aur user-friendly search option bhi diya gaya hai.

# ------------------ Naive Search (Linear Search) ------------------
def naive_search(lst, target):
    """
    Naive search: Har element ko iterate kar k check karta hai.
    Time Complexity: O(n) - Slow for large lists.
    """
    for i, item in enumerate(lst):
        if item == target:
            return i
    return -1


# ------------------ Recursive Binary Search ------------------
def binary_search(lst, target, low=0, high=None):
    """
    Recursive Binary Search: Fast search for sorted lists.
    Time Complexity: O(log n) - Efficient for large lists.
    """
    if high is None:
        high = len(lst) - 1

    if low > high:  # Base case: agar low high se bada hojaye
        return -1

    midpoint = (low + high) // 2

    if lst[midpoint] == target:
        return midpoint
    elif target < lst[midpoint]:
        return binary_search(lst, target, low, midpoint - 1)
    else:
        return binary_search(lst, target, midpoint + 1, high)


# ------------------ Built-in Bisect Search ------------------
def builtin_bisect_search(lst, target):
    """
    Built-in Bisect Search: Python's built-in optimized binary search.
    Time Complexity: O(log n) - Efficient and optimized.
    """
    index = bisect_left(lst, target)

    # Check agar element actually present hai
    if index < len(lst) and lst[index] == target:
        return index
    return -1


# ------------------ Performance Testing ------------------
def performance_test():
    """
    Performance test: Saare search methods ka comparison on a large dataset.
    """
    length = 10000  # Length of the sorted list
    sorted_list = sorted(random.sample(range(-3 * length, 3 * length), length))

    print("\n---- Performance Testing on List of Length:", length, "----")

    # Naive Search Test
    start = time.perf_counter()
    for target in sorted_list:
        naive_search(sorted_list, target)
    print(f"Naive Search Time: {time.perf_counter() - start:.4f} seconds")

    # Recursive Binary Search Test
    start = time.perf_counter()
    for target in sorted_list:
        binary_search(sorted_list, target)
    print(f"Recursive Binary Search Time: {time.perf_counter() - start:.4f} seconds")

    # Built-in Bisect Search Test
    start = time.perf_counter()
    for target in sorted_list:
        builtin_bisect_search(sorted_list, target)
    print(f"Built-in Bisect Search Time: {time.perf_counter() - start:.4f} seconds")


# ------------------ User Search Function ------------------
def user_search():
    """
    User search: Target number ko search karne k liye interactive method.
    """
    sorted_list = sorted(random.sample(range(-1000, 1000), 100))
    print("\n---- Sorted List Generated (Length = 100) ----")
    print(sorted_list)

    # User se target input lena with validation
    while True:
        try:
            target = int(input("\nApni search value enter karein (integer): "))
            break
        except ValueError:
            print("Invalid input! Sirf integer value enter karein.")

    print("\nSearch method select karein:")
    print("1. Naive Search (Linear Search)")
    print("2. Recursive Binary Search")
    print("3. Built-in Bisect Search")

    method_map = {
        "1": "naive",
        "2": "binary",
        "3": "bisect",
        "naive": "naive",
        "binary": "binary",
        "bisect": "bisect"
    }

    # Method selection with validation
    while True:
        method = input("Method select karein (1, 2, 3 ya naam): ").strip().lower()
        if method in method_map:
            method = method_map[method]
            break
        else:
            print("Invalid method! Sirf '1', '2', '3' ya method names (naive, binary, bisect) use karein.")

    # Search method apply karna
    if method == "naive":
        result = naive_search(sorted_list, target)
    elif method == "binary":
        result = binary_search(sorted_list, target)
    else:
        result = builtin_bisect_search(sorted_list, target)

    if result != -1:
        print(f"🎯 Target {target} found at index {result}.")
    else:
        print("❌ Target not found in the list.")


# ------------------ Main Program Execution ------------------
if __name__ == "__main__":
    print("\n================= Advanced Binary Search Project =================")
    print("1. Performance Test")
    print("2. User Search\n")

    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        performance_test()
    elif choice == "2":
        user_search()
    else:
        print("Invalid choice! Program terminated.")
