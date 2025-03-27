def main():
    # User se saal ka input lena
    year = int(input("Please input a year: "))

    # Leap year check karne ka logic
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("That's a leap year!")
    else:
        print("That's not a leap year!")


# Yeh line program ko run karne ke liye zaroori hai
if __name__ == '__main__':
    main()
