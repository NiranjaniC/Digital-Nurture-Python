"""
Import Standard Module
• Objective: Use the math module inside a function with validation + formatted output.
• Task: Calculate the area of a circle using math.pi and a given radius.
"""
import math
def calculate_area(radius):
    if not isinstance(radius,(int,float)):
        print("Invalid input")
        return
    if radius<0:
        print ("radius must be non-negative")
        return
    
    area = math.pi*radius*radius
    print(f"Area of the Circle: {area:.2f}")
calculate_area(5)
