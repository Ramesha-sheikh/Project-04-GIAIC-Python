import random  # Random numbers generate karne ke liye

def roll_dice():
    die1 = random.randint(1, 6)  # Pehla dice (1 se 6 tak random number)
    die2 = random.randint(1, 6)  # Dusra dice (1 se 6 tak random number)
    total = die1 + die2  # Dono dice ka sum
    print("Total of two dice:", total)  # Result print karo

def main():
    die1:int=10
    print("die1 in main() is: " + str(die1)) 
    roll_dice()  # Pehli baar roll
    roll_dice()  # Doosri baar roll
    roll_dice()  # Teesri baar roll
    print("die1 in main() is: " + str(die1))

if __name__ == '__main__':
    main()  # Program start hoga
