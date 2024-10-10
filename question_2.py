# Using a function, create a program that calculates the volume of a cylinder

import math
radius = float(input("Enter the radius: "))
height = float(input("Enter the height: "))
pie = math.pi
volume = pie * radius**2 * height
print(f"The volume of the cylinder with radius {radius} and height {height} is {volume:.2f}")