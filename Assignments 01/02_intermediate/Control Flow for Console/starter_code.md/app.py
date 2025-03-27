import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    while True:  
        # TODO: Ek random number generate kare jo 1 se 100 ke darmiyan ho
        secret_number = random.randint(1, 100)
        print("Maine 1 se 100 tak ka ek number select kiya hai. Guess karo!")

        # TODO: User ko NUM_ROUNDS (5) attempts de taake wo number guess kar sake
        for attempt in range(1, NUM_ROUNDS + 1):
            try:
                # TODO: User ka input le aur check kare ke wo sahi hai ya nahi
                guess = int(input(f"Attempt {attempt}/{NUM_ROUNDS}: Apna guess enter karo: "))
                
                # TODO: Agar guess chhota ho to "Too low" ka message de
                if guess < secret_number:
                    print("Bohat chhota! Phir se try karo.")
                # TODO: Agar guess bara ho to "Too high" ka message de
                elif guess > secret_number:
                    print("Bohat bara! Phir se try karo.")
                # TODO: Agar guess sahi ho to user ko mubarakbaad de aur loop se bahar nikal aaye
                else:
                    print(f"Mubarak ho! Tumne sahi number {secret_number} {attempt} attempt(s) mein guess kar liya.")
                    break
            except ValueError:
                print("Ghalat input! Sirf number enter karo.")

        else:
            # TODO: Agar sare attempts khatam ho jayein to user ko correct number bata de
            print(f"Afsos, tumhare {NUM_ROUNDS} attempts khatam ho gaye. Sahi number {secret_number} tha.")

        # TODO: User se puchhe ke kya wo dobara khelna chahta hai ya nahi
        play_again = input("Kya tum dobara khelna chahoge? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Shukriya khelne ka! Allah Hafiz.")
            break

if __name__ == "__main__":
    main()
