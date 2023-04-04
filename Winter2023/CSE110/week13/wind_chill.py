import math

def compute_wind_chill (speed, temperature):
    return 35.74 + 0.615 * temperature - 35.75 * (speed ** 0.16) + 0.4275 * temperature * (speed ** 0.10)

def convert (Celsius):
    return Celsius * (9/5) + 32

temperature = int(input('What is the temperature? '))
measurement = input('Fahrenheit or Celsius (F/C)? ')