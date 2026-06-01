"""
Numeric Input
• Objective: Convert user input to a number with validation + function + formatted
output.
• Task: Ask user for age, validate, convert to integer, and print next year’s age.
"""
def age_calculator(age):
    if age == "":
        print("Age is empty")
        return
    if not age.isdigit():
        print("Invalid age")
        return
    age = int(age)
    if(age <=0):
        print("Age must be greater than 0")
        return
    print(f"Next year you'll be {age+1}")
age = input("Enter your age:")
age_calculator(age)
