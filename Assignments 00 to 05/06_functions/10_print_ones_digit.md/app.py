# Function to print the ones digit of a given number
def print_ones_digit(num: int):
    # Calculate and print the ones digit using the modulo operator
    print("The ones digit is", num % 10)

# Main function to take user input and call the print_ones_digit function
def main():
    # Ask the user to enter a number
    num = int(input("Enter a number: "))
    
    # Call the helper function to display the ones digit
    print_ones_digit(num)

# Ensure the program runs only when executed directly
if __name__ == '__main__':
    main()
