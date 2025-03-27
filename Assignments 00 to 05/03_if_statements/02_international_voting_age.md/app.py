# Define the minimum voting ages for the three countries
PETURKSBOUIPO_AGE: int = 16
STANLAU_AGE: int = 25
MAYENGUA_AGE: int = 48

def main():
    """
    Asks the user for their age and tells them where they can and cannot vote.
    """
    # Get the user's age as an integer
    user_age = int(input("How old are you? "))

    # Check voting eligibility for Peturksbouipo
    if user_age >= PETURKSBOUIPO_AGE:
        print(f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
    
    # Check voting eligibility for Stanlau
    if user_age >= STANLAU_AGE:
        print(f"You can vote in Stanlau where the voting age is {STANLAU_AGE}.")
    else:
        print(f"You cannot vote in Stanlau where the voting age is {STANLAU_AGE}.")
    
    # Check voting eligibility for Mayengua
    if user_age >= MAYENGUA_AGE:
        print(f"You can vote in Mayengua where the voting age is {MAYENGUA_AGE}.")
    else:
        print(f"You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}.")

# This ensures that the script runs only when executed directly
if __name__ == '__main__':
    main()
