def get_user_numbers():
    user_numbers = []
    while True:
        user_input = input("Enter a number (press enter to stop): ")
        
        if user_input == "":  # Agar input blank ho, loop break ho jaye
            break

        try:
            num = int(user_input)
            user_numbers.append(num)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    return user_numbers


def count_nums(num_lst):
    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    
    return num_dict


def print_counts(num_dict):
    for num, count in num_dict.items():
        print(f"{num} appears {count} times.")


def main():
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)


# Program ko run karne ke liye zaroori line
if __name__ == '__main__':
    main()
