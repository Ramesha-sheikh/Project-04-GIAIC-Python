# Using F-strings (Python 3.6+)
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Your favorite hobby: ")
current_year = 2024
birth_year = current_year - age

print(f"\nHello, {name}! You are {age} years old and were born in {birth_year}.")
print(f"Great to know you love {hobby}!")
print(f"In 5 years, you'll be {age + 5}!")

# Using % Formatting (Old Style)
print("\n--- Using % Formatting ---")
print("Hello, %s! You are %d years old and were born in %d." % (name, age, birth_year))
print("It's awesome that you love %s!" % hobby)
print("In 5 years, you'll be %d!" % (age + 5))

# Using .format() Method
print("\n--- Using .format() Method ---")
print("Hello, {}! You are {} years old and were born in {}.".format(name, age, birth_year))
print("It's great that you enjoy {}!".format(hobby))
print("In 5 years, you'll be {}!".format(age + 5))
