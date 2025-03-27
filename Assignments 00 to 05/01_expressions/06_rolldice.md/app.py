import random

dic_side =6

def main():
    die1: int = random.randint(1, dic_side)
    die2: int = random.randint(1, dic_side)
    total: int = die1 + die2
    print("Dice have", dic_side, "sides each.")

    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)
if __name__ == '__main__':
    main()