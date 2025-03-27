def main():
    C = 299792458  # Speed of light in meters per second
    
    while True:
        mass = float(input("Enter kilos of mass (or 0 to exit): "))  # User se mass lena
        if mass == 0:
            break  # Agar 0 enter kare to loop exit kare
        
        energy = mass * C**2  # Einstein's equation
        print(f"\nm = {mass} kg")
        print(f"C = {C} m/s")
        print(f"{energy} joules of energy!\n")

if __name__ == '__main__':
    main()
