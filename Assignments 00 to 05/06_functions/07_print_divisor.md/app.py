def print_divisors(num: int):
    print(f"Here are the divisors of {num}: ", end="")  # Divisors ko ek hi line pe dikhane ke liye
    for i in range(1, num + 1):  # 1 se num tak loop chalayenge
        if num % i == 0:  # Agar remainder 0 hai, to divisor hai
            print(i, end=" ")  # Divisor ko print karenge, space ke sath


def main():
    num = int(input("Enter a number: "))  # User se input le rahe hain
    print_divisors(num)  # Helper function ko call karenge


# Program run karne ke liye required line
if __name__ == '__main__':
    main()
