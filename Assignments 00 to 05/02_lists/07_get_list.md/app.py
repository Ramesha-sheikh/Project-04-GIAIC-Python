def main():
    lst = []  # Ek khaali list banayein jisme values store hongi

    val = input("Enter a value: ")  # Pehli value user se lein
    while val:  # Jab tak user enter daba kar khaali input na de
        lst.append(val)  # Value ko list me add karein
        val = input("Enter a value: ")  # Agli value lene ke liye prompt karein

    print("Here's the list:", lst)  # Akhir me puri list print karein


# Neeche diye gaye code ko badalne ki zaroorat nahi hai

if __name__ == '__main__':
    main()
