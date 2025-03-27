# Constants for planetary gravity multipliers
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

def main():
    # Step 1: User se Earth ka weight lena
    earth_weight = float(input("Enter a weight on Earth: "))

    # Step 2: User se ek planet ka naam lena
    planet = input("Enter a planet: ").strip()

    # Step 3: Select the correct gravity multiplier
    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    elif planet == "Neptune":
        gravity_constant = NEPTUNE_GRAVITY
    else:
        print("Invalid planet name! Please enter a correct planet.")
        return  # Exit function if input is invalid

    # Step 4: Calculate planetary weight
    planetary_weight = round(earth_weight * gravity_constant, 2)

    # Step 5: Print output
    print("The equivalent weight on " + planet + ": " + str(planetary_weight))

if __name__ == "__main__":
    main()
