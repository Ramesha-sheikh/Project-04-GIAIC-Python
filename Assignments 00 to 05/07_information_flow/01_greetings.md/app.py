# Helper function to greet the user
def greet(name: str) -> str:
    return "Greetings " + name + "!"

# Main function to get user's name and greet them
def main():
    name: str = input("What's your name? ")
    print(greet(name))

# Ensures the program runs only when executed directly
if __name__ == '__main__':
    main()
