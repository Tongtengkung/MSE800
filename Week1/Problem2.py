import numpy as np

def calculate_bmi(weight, height):                                 # Function to calculate BMI
    return weight / (height ** 2)

weight = float(input("Please enter your weight in kilograms: "))   # Get user input for weight and height
height = float(input("Please enter your height in meters: "))

bmi = calculate_bmi(weight, height)                                # Calculate BMI

print(f"Your Body Mass Index (BMI) is: {bmi:.2f}")                 # Print the BMI result using f-string