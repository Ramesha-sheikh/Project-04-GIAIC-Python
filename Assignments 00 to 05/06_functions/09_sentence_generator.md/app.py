# Helper function to generate sentences based on part of speech
def make_sentence(word: str, part_of_speech: int):
    if part_of_speech == 0:  # Check if the input is a noun
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:  # Check if the input is a verb
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:  # Check if the input is an adjective
        print(f"Looking out my window, the sky is big and {word}!")
    else:  # Handle invalid input
        print("Part of speech must be 0, 1, or 2! Can't make a sentence.")

# Main function to take input from the user and call make_sentence
def main():
    # Ask the user to input a word
    word = input("Please type a noun, verb, or adjective: ")
    
    # Prompt the user to enter the part of speech (0, 1, or 2)
    print("Is this a noun, verb, or adjective?")
    part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
    
    # Call the helper function with the given word and part of speech
    make_sentence(word, part_of_speech)

# Ensure the program runs only when executed directly, not when imported
if __name__ == '__main__':
    main()
