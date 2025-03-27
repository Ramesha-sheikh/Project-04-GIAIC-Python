
# import random # type: ignore

# my_number=random.randint(0,99)
# # print(my_number)

# while True:
#  user_input=int(input("Enter your number:"))
#  if(user_input < my_number):
#     print("too low try again")
#  elif(user_input > my_number):
#     print("too high try again.")
#  else:
#     print("your guess is correct.")
#     break





import random

def guess_the_number():
    print("Welcome to 'Guess the Number' game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")
            
guess_the_number()





