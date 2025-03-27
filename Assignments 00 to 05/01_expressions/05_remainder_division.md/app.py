def main():
    # Get the numbers we want to divide
    num1: int = int(input("Please enter an integer to be divided: "))
    num2: int = int(input("Please enter an integer to divide by: "))

    result: int = num1 // num2  # Divide with no remainder/decimals (integer division)
    mod: int = num1 % num2  # Get the remainder of the division (modulo)
    
    print("The result of this division is " + str(result) + " with a remainder of " + str(mod))


if __name__ == '__main__':
    main()
