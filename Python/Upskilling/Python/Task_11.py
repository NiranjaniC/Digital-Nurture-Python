"""
Float Input
Objective: Handle decimal input with validation + function + formatted output.
Task: Convert weight from kilograms to pounds.
"""
def convert_weight():
    weight = input("Enter weight is kg: ")
    if(weight == ""):
        print("weight cannot be empty")
        return
    try:
        weight = float(weight)
    except ValueError:
        print("Invalid input!")
        return
    if weight <= 0:
        print("weight must be greater than zero")
        return
    pounds = weight*2.20462
    print(f"Weight in kg : {weight}")
    print(f"Weight  in lbs : {pounds:.2f}")
convert_weight()