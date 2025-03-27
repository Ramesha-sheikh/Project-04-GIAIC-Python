import random

def main():
    # Generate a random secret number between 1 and 99
    secret_number = random.randint(1, 99)
    print("I am thinking of a number between 1 and 99...")

    # Take the first guess from the user
    guess = int(input("Enter your first guess: "))

    # Loop continues until the guess matches the secret number
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low!")
        else:
            print("Your guess is too high!")
        
        # Ask for a new guess
        guess = int(input("Enter a new guess: "))

    # Congratulate the user when they guess correctly
    print(f"Congrats! You guessed it right. The number was: {secret_number}")

if __name__ == '__main__':
    main()
