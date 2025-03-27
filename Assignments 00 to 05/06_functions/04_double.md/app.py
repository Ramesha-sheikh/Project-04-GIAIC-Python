def double(num: int):
    """
    Yeh function diye gaye number ka double return karta hai.
    """
    return num * 2  # Number ko 2 se multiply karke return kar raha hai


def main():
    number = int(input("Enter a number: "))  # User se number input lena
    doubled_value = double(number)  # double() function ko call karke value lena
    print("Double that is", doubled_value)  # Result ko print karna


# Program run karne ke liye zaroori line
if __name__ == '__main__':
    main()
