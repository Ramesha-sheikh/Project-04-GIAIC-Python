def main():
    # Ek list banani hai jisme yeh fruits hon: 'apple', 'banana', 'orange', 'grape', 'pineapple'.
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # List ki length print karni hai.
    print("Length of fruit list:", len(fruit_list))
    
    # List ke end par 'mango' add karna hai.
    fruit_list.append('mango')
    
    # Updated list print karni hai.
    print("Updated fruit list:", fruit_list)

def access_element(lst, index):
    """Diye gaye index par element return karega."""
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Index out of range!"

def modify_element(lst, index, new_value):
    """Diye gaye index par element ko naye value se replace karega."""
    if 0 <= index < len(lst):
        lst[index] = new_value
        return "Element updated!"
    else:
        return "Index out of range!"

def slice_list(lst, start, end):
    """Start aur end index ke darmiyan wale elements ki new list return karega."""
    return lst[start:end]

def game():
    """Ek text-based game jo list ke sath interact karne ka moka dega."""
    my_list = ['red', 'blue', 'green', 'yellow', 'purple']
    
    while True:
        print("\nCurrent List:", my_list)
        print("Choose an operation:")
        print("1. Kisi element ko access karein")
        print("2. Kisi element ko modify karein")
        print("3. List ka ek hissa slice karein")
        print("4. Game exit karein")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            index = int(input("Enter index to access: "))
            print("Element:", access_element(my_list, index))
        elif choice == '2':
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            print(modify_element(my_list, index, new_value))
        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced list:", slice_list(my_list, start, end))
        elif choice == '4':
            print("Game exit ho raha hai.")
            break
        else:
            print("Invalid choice! Dobara select karein.")

if __name__ == "__main__":
    main()
    game()
