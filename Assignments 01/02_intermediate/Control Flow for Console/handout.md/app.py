import random

def get_user_choice():
    while True:
        choice = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
        if choice in ["higher", "lower"]:
            return choice
        print("Invalid input! Please enter either 'higher' or 'lower'.")

def play_game(num_rounds=5):
    score = 0
    print("Welcome to the High-Low Game!\n--------------------------------")
    
    for round_num in range(1, num_rounds + 1):
        print(f"Round {round_num}")
        user_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        
        print(f"Your number is {user_number}")
        user_guess = get_user_choice()
        
        if (user_guess == "higher" and user_number > computer_number) or \
           (user_guess == "lower" and user_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        print(f"Your score is now {score}\n")
    
    print("Thanks for playing!")
    
    if score == num_rounds:
        print("Wow! You played perfectly!")
    elif score >= num_rounds // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

# Run the game with 5 rounds
play_game(5)
