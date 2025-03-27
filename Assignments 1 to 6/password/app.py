import random  # Random module ko import karte hain, yeh random selection ke liye use hota hai
import string  # String module ko import karte hain, yeh predefined characters ka set provide karta hai

# Function to generate a single random password
def generate_password(length):
    # Yeh saare characters ko ek string mein combine kar raha hai: letters (uppercase + lowercase), digits, punctuation
    all_characters = string.ascii_letters + string.digits + string.punctuation  
    
    # Randomly length jitne characters select karke password bana rahe hain
    password = ''.join(random.choice(all_characters) for _ in range(length))  
    
    return password  # Generated password ko return karte hain

# Function to generate multiple passwords
def generate_multiple_passwords():
    while True:  # Jab tak sahi input na aaye, loop chalta rahega
        try:
            num_passwords = int(input("How many passwords do you want to generate? "))  # Input ko integer mein convert karte hain
            length = int(input("Enter the length of each password: "))  # Password ka length bhi integer hoga
            break  # Agar input sahi ho, toh loop se nikal jaayein
        except ValueError:  # Agar input valid nahi hai toh error message show kare
            print("Invalid input! Please enter a valid number.")

    print("\nGenerated Passwords:")  # Generated passwords ko display karne ka heading
    for _ in range(num_passwords):  # Jitne passwords user ne bola, utni dafa loop chalega
        print(generate_password(length))  # Har generated password ko print karte hain

# Program ko start karne ke liye function ko call karte hain
generate_multiple_passwords()
