
#milstone 1 

def main():
    # Step 1: User se Earth ka weight input lena
    weight_on_earth = float(input("Enter your weight on Earth: "))

    # Step 2: Mars ka weight calculate karna
    weight_on_mars = weight_on_earth * 0.378

    # Step 3: Output ko 2 decimal places tak round karna
    weight_on_mars = round(weight_on_mars, 2)

    # Step 4: Result print karna
    print(f"The equivalent weight on Mars: {weight_on_mars}")

if __name__ == "__main__":
    main()

def calculate_weight(weight, planet):
    # Har planet ka gravity factor dictionary mein store karna
    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    # Check karna ke user ne valid planet enter kiya hai ya nahi
    if planet in gravity_factors:
        return round(weight * gravity_factors[planet], 2)
    else:
        return None  # Agar planet invalid ho to None return karna

def main():
    # Step 1: User se Earth ka weight lena
    weight_on_earth = float(input("Enter your weight on Earth: "))

    # Step 2: User se ek planet ka naam lena
    planet = input("Enter a planet: ").strip()

    # Step 3: Selected planet ka weight calculate karna
    weight_on_planet = calculate_weight(weight_on_earth, planet)

    # Step 4: Output print karna
    if weight_on_planet is not None:
        print(f"The equivalent weight on {planet}: {weight_on_planet}")
    else:
        print("Invalid planet! Please enter a correct planet name.")

if __name__ == "__main__":
    main()
