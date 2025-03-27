def get_user_info():
    first_name: str = input("What is your first name?: ")
    last_name: str = input("What is your last name?: ")
    email_address: str = input("What is your email address?: ")

    # Returning multiple values as a tuple
    return first_name, last_name, email_address


def main():
    # Receiving and displaying the returned tuple
    user_data = get_user_info()
    print("Received the following user data:", user_data)


if __name__ == "__main__":
    main()
