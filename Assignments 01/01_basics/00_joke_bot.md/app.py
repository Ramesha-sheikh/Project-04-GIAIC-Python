PROMPT = "What do you want? "
JOKE = "Here is a programming joke for you! Why do Java developers wear glasses? Because they don't C# 😂"
SORRY = "Sorry, I only tell programming jokes."

def main():
    user_input = input(PROMPT)  # 🔹 Pehle user se input lo
    user_input = user_input.strip().lower()  # 🔹 Extra spaces hatao aur lowercase me convert karo
    
    if "joke" in user_input:
        print(JOKE)  # 🔹 Agar "joke" likha ho, toh programming joke print karo
    else:
        print(SORRY)  # 🔹 Agar kuch aur likha ho, toh sorry message print karo

if __name__ == "__main__":
    main()
