def get_first_element(lst):
    """
    Diye gaye list ka pehla element print karta hai.
    """
    print(lst[0])

# Neeche diye gaye code ko badalne ki zaroorat nahi hai

def get_lst():
    """
    User se ek ek karke list ke elements lene ka kehata hai aur akhir mein list return karta hai.
    """
    lst = []
    elem: str = input("Ek element daalein ya rukne ke liye enter press karein. ")
    while elem != "":
        lst.append(elem)
        elem = input("Ek element daalein ya rukne ke liye enter press karein. ")
    return lst

def main():
    """
    List hasil karne aur uska pehla element dikhane ka kaam karta hai.
    """
    lst = get_lst()
    get_first_element(lst)

if __name__ == '__main__':
    main()
