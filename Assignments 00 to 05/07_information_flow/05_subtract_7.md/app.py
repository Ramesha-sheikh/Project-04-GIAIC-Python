def main():
    # Initialize a variable 'num' with value 7
    num: int = 7

    # Call the helper function to subtract 7 from 'num'
    num = subtract_seven(num)

    # Print the result after subtraction
    print("This should be zero:", num)


def subtract_seven(num):
    # Subtract 7 from the given number
    num = num - 7

    # Return the result
    return num


# Standard practice to call main() when the script runs
if __name__ == '__main__':
    main()
