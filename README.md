# Weight calculator on other planets
# Calculates how much a person would weigh on different planets in the solar system

# Relative gravity of each planet compared to Earth's
planet_gravity = {
    "Mercury": 0.38,
    "Venus": 0.91,
    "Earth": 1.0,
    "Mars": 0.38,
    "Jupiter": 2.34,
    "Saturn": 1.06,
    "Uranus": 0.92,
    "Neptune": 1.19
}

# Asks for the person's weight on Earth
earth_weight = float(input("Enter your weight on Earth (in kg): "))

print("\nYour weight on each planet would be:")

# Calculates and displays the weight on each planet
for planet, gravity in planet_gravity.items():
    weight_on_planet = earth_weight * gravity
    print(f"{planet}: {weight_on_planet:.1f} kg")
