import random
from collections import defaultdict

class MarkovChain:
    def __init__(self):
        self.graph = defaultdict(list)
        self.start_words = []

    def train(self, text):
        words = text.split()
        if len(words) < 2:
            return
        
        self.start_words.append(words[0])
        
        for i in range(len(words) - 2):
            key = (words[i], words[i + 1])  # Bigram (2 words as key)
            self.graph[key].append(words[i + 2])

    def generate_text(self, length=10):
        if not self.start_words:
            return "No training data available."

        key = random.choice(list(self.graph.keys()))  # Random bigram start
        sentence = [key[0], key[1]]

        for _ in range(length - 2):
            if key in self.graph:
                next_word = random.choice(self.graph[key])
                sentence.append(next_word)
                key = (key[1], next_word)  # Shift key to next bigram
            else:
                break

        return " ".join(sentence)
