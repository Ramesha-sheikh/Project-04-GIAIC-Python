def print_multiple(message: str, repeats: int):
    for _ in range(repeats):  # Loop chalega jitni dafa repeat karna hai
        print(message)  # Message ko print karenge


def main():
    message = input("Please type a message: ")  # User se message input
    repeats = int(input("Enter a number of times to repeat your message: "))  # Repeat times input
    print_multiple(message, repeats)  # Function ko call karenge


# Program run karne ke liye required line
if __name__ == '__main__':
    main()
