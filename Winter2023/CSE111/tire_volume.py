import math

width = float(input("Enter the width of the tire in mm: "))
aspectRatio = float(input("Enter the aspect ratio of the tire: "))
diameter = float(input("Enter the diameter of the tire in inches: "))

volume = (math.pi * width**2 * aspectRatio (width * aspectRatio + 2540 * diameter) )/10,000,000,000

print(f"The approximate volume of the tire is {volume} liters")
