import random  # Random module for computer's choice

# Ek round khelne ka function
def play_round():
    choices = ['rock', 'paper', 'scissors']  # Valid choices ka list

    # User se input lena
    user_choice = input("Apna choice likhein (rock, paper, scissors): ").lower()

    # Input check karna
    if user_choice not in choices:
        print("Invalid choice! Sirf 'rock', 'paper', ya 'scissors' likhein.")
        return  # Invalid input pe function end ho jayega

    # Computer ka random choice
    computer_choice = random.choice(choices)
    print(f"Computer ka choice: {computer_choice}")

    # Winner check karna
    if user_choice == computer_choice:
        print("Match tie ho gaya!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("Aap jeet gaye! 🎉")
    else:
        print("Aap haar gaye! 😢")

# Game ko multiple rounds tak chalane ka function
def play_game():
    print("Rock, Paper, Scissors khelne ka shukriya! 😊")

    while True:  # Jab tak user quit na karay, game chalti rahegi
        play_round()  # Ek round khelna

        # User se poochna agar dubara khelna chahta hai
        play_again = input("Dubara khelna hai? (yes/no): ").lower()

        # Agar answer 'yes' nahi hai to game khatam
        if play_again != 'yes':
            print("Thanks for playing! Allah Hafiz!")
            break

# Game start karna
play_game()
