import time

def countdown_timer():
    while True:
        try:
            # Countdown time ko integer mein convert karne ki koshish
            countdown_time = int(input("Countdown time (seconds mein) likhein (sirf number): "))
            break  # Agar sahi input ho, toh loop break ho jaye
        except ValueError:
            print("⛔ Ghalat input! Sirf number likhein, dobara try karein.")  # Jab non-numeric input ho

    # Countdown loop
    while countdown_time > 0:
        print(f"Baaki time: {countdown_time} seconds")
        time.sleep(1)
        countdown_time -= 1

    print("⏰ Time's up! Timer khatam ho gaya!")  # Jab timer khatam ho jaye

# Timer ko start karna
countdown_timer()
