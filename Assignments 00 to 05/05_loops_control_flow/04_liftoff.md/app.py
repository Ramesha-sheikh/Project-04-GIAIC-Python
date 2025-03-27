def main():
    # Countdown starts from 10 to 1 (inclusive)
    for i in range(10, 0, -1):  # The range starts at 10, ends at 1, decrementing by -1
        print(i, end=' ')  # Print the countdown number followed by a space
    
    print("Liftoff!")  # After the countdown, print "Liftoff!"

# Entry point to execute the main function
if __name__ == '__main__':
    main()
