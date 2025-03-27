# Constant string for the affirmation message
AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    # Prompt the user to type the affirmation
    print("Please type the following affirmation: " + AFFIRMATION)
    
    # Get user input
    user_feedback = input()

    # Keep asking until the user types the correct affirmation
    while user_feedback != AFFIRMATION:
        print("That was not the affirmation.")  # Inform about incorrect input
        print("Please type the following affirmation: " + AFFIRMATION)  # Prompt again
        user_feedback = input()  # Get input again
    
    # Congratulate the user for typing correctly
    print("That's right! :)")

# Entry point to execute the main function
if __name__ == '__main__':
    main()
