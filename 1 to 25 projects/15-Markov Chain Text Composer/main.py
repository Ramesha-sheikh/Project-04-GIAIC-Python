import os
from src.markov_chain import MarkovChain

if __name__ == "__main__":
    file_path = "data/input.txt"

    if not os.path.exists(file_path):
        print("Error: Training file not found.")
        exit()

    with open(file_path, "r", encoding="utf-8") as file:
        training_text = file.read()

    markov = MarkovChain()
    markov.train(training_text)

    print(markov.generate_text(length=20))  # Increase text length
