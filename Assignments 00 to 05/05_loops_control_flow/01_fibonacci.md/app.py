# Maximum value for Fibonacci sequence
MAX_TERM_VALUE: int = 10000

def main():
    # Initializing the first two terms of the Fibonacci sequence
    curr_term = 0  # Fib(0)
    next_term = 1  # Fib(1)

    # Loop until the current term exceeds the maximum value
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ")  # Print the current term with a space

        # Calculate the next term in the sequence
        term_after_next = curr_term + next_term

        # Update values for the next iteration
        curr_term = next_term
        next_term = term_after_next

# Required line to start the main function
if __name__ == '__main__':
    main()
