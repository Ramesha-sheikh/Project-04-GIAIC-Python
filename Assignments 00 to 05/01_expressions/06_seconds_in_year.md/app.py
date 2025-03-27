DAYS_PER_YEAR: int = 365  # 1 saal mein 365 din hote hain
HOURS_PER_DAY: int = 24   # 1 din mein 24 ghante hote hain
MIN_PER_HOUR: int = 60    # 1 ghante mein 60 minutes hote hain
SEC_PER_MIN: int = 60     # 1 minute mein 60 seconds hote hain

def main():
    # Multiplication se total seconds calculate karna
    total_seconds = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN

    # Result print karna
    print("There are " + str(total_seconds) + " seconds in a year!")
if __name__ == '__main__':
    main()
