MINIMUM_HEIGHT = 50  # Minimum height ka requirement

def main():
    while True:
        # User se height ka input lena
        height_input = input("How tall are you? (Press Enter to exit): ")

        # Agar user ne kuch bhi nahi likha, toh program exit ho jayega
        if height_input == "":
            print("Exiting the program. Goodbye!")
            break

        # Height ko float mein convert karna
        height = float(height_input)

        # Height check karna
        if height >= MINIMUM_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

# Yeh line program ko run karne ke liye zaroori hai
if __name__ == '__main__':
    main()
