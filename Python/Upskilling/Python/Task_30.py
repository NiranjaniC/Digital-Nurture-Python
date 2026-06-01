"""
Basic Try-Except
• Objective: Catch simple runtime errors using try-except with a function and clear
output.
• Task: Safely divide two numbers and handle division-by-zero errors.
"""
def divide_numbers(num1,num2):
    try:
        result = num1/num2
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero")
divide_numbers(10,0)