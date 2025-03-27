# Markov Chain Text Composer

## Overview
This project is a simple text generator using a Markov Chain model. It learns from a given text dataset and generates new text based on word probabilities.

## Features
- Implements Markov Chains for text generation.
- Supports training from a text file.
- Randomized sentence generation with adjustable length.
- Works with Python's built-in libraries (no external dependencies).

## Installation
Ensure you have **Python 3.10+** installed.

Clone the repository and navigate to the project directory:
```sh
mkdir MarkovChainComposer
cd MarkovChainComposer
```

## Folder Structure
```
MarkovChainComposer/
│── data/
│   ├── input.txt  # Training data (text source for Markov Chain)
│── src/
│   ├── markov_chain.py  # Markov Chain logic and text generation
│── main.py  # Main script to run the text generator
│── requirements.txt  # Dependencies file (currently not needed)
│── README.md  # Documentation and usage instructions
```

## Dependencies
This project uses Python's built-in modules, so no additional libraries are required:
- `os` - For handling file paths and system interactions.
- `random` - For randomly selecting words based on probabilities.
- `collections.defaultdict` - For efficient graph storage.

## Usage
1. **Prepare Training Data**
   - Add text data to `data/input.txt`. This file serves as the dataset for training the Markov Chain.
   
2. **Run the Script**
   - Open a terminal in the project directory and execute:
     ```sh
     python main.py
     ```
   - The script will generate a random sentence based on the input data.

## Example Output
```
I love programming because it is fun and exciting.
```

## Customization
- **Change Sentence Length:** Edit `main.py` and modify the length parameter:
  ```python
  print(markov.generate_text(length=20))  # Generate longer text
  ```
- **Change Start Word:** Modify the starting word in `main.py` for different outputs.

## License
This project is open-source. Feel free to modify and improve!
