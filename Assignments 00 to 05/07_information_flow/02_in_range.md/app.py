def in_range(n: int, low: int, high: int) -> bool:
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    return low <= n <= high  # Using a concise comparison


def main():
    n = int(input("Enter the number to check: "))
    low = int(input("Enter the lower limit: "))
    high = int(input("Enter the upper limit: "))
    
    if in_range(n, low, high):
        print(f"{n} is within the range {low} to {high}.")
    else:
        print(f"{n} is NOT within the range {low} to {high}.")


# Ensures the program runs only when executed directly
if __name__ == '__main__':
    main()
