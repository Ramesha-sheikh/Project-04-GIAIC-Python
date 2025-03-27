import random  # Random module ko import karte hain

# Possible words list
word_list = ["python", "java", "javascript", "hangman", "developer", "coding"]

# Hangman game ka function
def hangman():
    word = random.choice(word_list)  # Random word select hota hai
    guessed_word = ["_"] * len(word)  # Word ko pehle underscores mein show karte hain
    guessed_letters = []  # Guessed letters ka list
    incorrect_guesses = 0  # Ghalat guesses ka counter
    max_wrong_guesses = 6  # Max allowed ghalat guesses

    print("👋 Welcome to Hangman Game!")
    print("Aap ko ek hidden word guess karna hai.")
    print(" ".join(guessed_word))  # Pehle underscores dikhate hain

    while incorrect_guesses < max_wrong_guesses:
        guess = input("Ek letter guess karein: ").lower()  # Input ko lowercase mein convert karte hain

        # Invalid input check: sirf aik letter aur alphabet ho
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Sirf aik alphabet likhein! Dobara try karein.")
            continue

        # Already guessed letter check
        if guess in guessed_letters:
            print("⛔ Yeh letter pehle hi guess ho chuka hai!")
            continue

        guessed_letters.append(guess)  # Guessed letter ko list mein add karte hain

        if guess in word:  # Agar guess sahi hai
            print(f"✅ Sahi guess! '{guess}' word mein shamil hai.")
            # Jahan jahan guess sahi hai, wahan update karte hain
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            incorrect_guesses += 1  # Ghalat guess ko count karte hain
            print(f"❌ Ghalat guess! {max_wrong_guesses - incorrect_guesses} tries baqi hain.")

        # Ab tak ka guessed word aur guessed letters dikhate hain
        print("Word: ", " ".join(guessed_word))
        print("Guessed letters: ", ", ".join(guessed_letters))

        # Agar poora word guess ho gaya
        if "_" not in guessed_word:
            print("🎉 Mubarak ho! Aap ne word guess kar liya! 👏")
            break

    # Agar max ghalat guesses ho jayein
    if incorrect_guesses == max_wrong_guesses:
        print(f"😢 Game Over! Sahi word tha: '{word}'.")

# Game start karte hain
hangman()
