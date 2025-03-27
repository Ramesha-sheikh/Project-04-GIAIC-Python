def read_phone_numbers():
    phonebook = {}

    while True:
        name = input("Enter name (leave blank to stop): ")
        if name == "":
            break

        number = input(f"Enter phone number for {name}: ")
        phonebook[name] = number

    return phonebook


def print_phonebook(phonebook):
    print("\nPhonebook Entries:")
    for name, number in phonebook.items():
        print(f"{name} -> {number}")


def lookup_numbers(phonebook):
    print("\nPhonebook Lookup:")
    while True:
        name = input("Enter name to lookup (leave blank to stop): ")
        if name == "":
            break
        if name in phonebook:
            print(f"{name}'s phone number is: {phonebook[name]}")
        else:
            print(f"{name} is not in the phonebook.")


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)


if __name__ == '__main__':
    main()
