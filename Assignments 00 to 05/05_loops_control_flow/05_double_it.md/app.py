def main():
    # Ask the user to enter a number
    curr_value = int(input("Enter a number: "))

    # Continue doubling until the value is 100 or greater
    while curr_value < 100:
        curr_value *= 2  # Double the current value
        print(curr_value, end=" ")  # Print the doubled value on the same line with a space

# Entry point to execute the main function
if __name__ == '__main__':
    main()
