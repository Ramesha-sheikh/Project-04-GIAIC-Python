# Define the maximum length the list should have
MAX_LENGTH: int = 3  

def shorten(lst):
    """
    Removes elements from the end of lst until its length becomes MAX_LENGTH.
    Prints each removed element.
    """
    while len(lst) > MAX_LENGTH:  # Continue removing elements until length is MAX_LENGTH
        last_elem = lst.pop()  # Removes and stores the last element
        print(last_elem)  # Prints the removed element

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []  # Initialize an empty list
    elem = input("Please enter an element of the list or press enter to stop: ")
    
    while elem != "":  # Keep taking input until the user presses enter
        lst.append(elem)  # Add the element to the list
        elem = input("Please enter an element of the list or press enter to stop: ")
    
    return lst  # Return the final list

def main():
    """
    Gets a list from the user and shortens it if necessary.
    """
    lst = get_lst()  # Get the list from user input
    shorten(lst)  # Call the shorten function to modify the list if needed

# Required to ensure the script runs when executed directly
if __name__ == '__main__':
    main()
