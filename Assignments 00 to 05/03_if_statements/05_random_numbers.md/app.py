import random

N_NUMBERS = 10     # Kitne numbers generate karne hain
MIN_VALUE = 1      # Minimum range
MAX_VALUE = 100    # Maximum range

def main():
    print("10 Random Numbers between 1 and 100:")
    
    # Loop se 10 random numbers print karna
    for _ in range(N_NUMBERS):
        random_number = random.randint(MIN_VALUE, MAX_VALUE)
        print(random_number, end=" ")

# Program run karne ke liye required line
if __name__ == '__main__':
    main()
