def count_even(lst):
    """
    Yeh function list mein se even numbers ko count karta hai
    """
    count = 0  # Even numbers ka count store karne ke liye
    for num in lst:  # List ke her number ko check karna
        if num % 2 == 0:  # Agar number even hai
            count += 1  # Even number milne par count ko increase karna

    print("Total even numbers:", count)  # Total even numbers print karna


def get_list_of_ints():
    """
    User se integers input lenay ka function jab tak woh enter na kare
    """
    lst = []  # Empty list banayi
    while True:  # Infinite loop, user enter karne par rukega
        user_input = input("Enter an integer or press enter to stop: ")

        if user_input == "":  # Agar enter press kare to loop se bahar nikle
            break

        lst.append(int(user_input))  # Input ko integer mein convert karke list mein daala

    return lst  # List ko return kiya


def main():
    lst = get_list_of_ints()  # User se list lenay wala function call kiya
    count_even(lst)  # Even numbers count karne ka function call kiya


# Program ko run karne ke liye zaroori line
if __name__ == '__main__':
    main()
