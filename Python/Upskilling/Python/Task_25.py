"""
25. Parameters
• Objective: Pass arguments into a function with validation + structured output.
• Task: Create a function that adds two numbers and prints the result.
"""
def add(a,b):
    # validate inputs
    if not isinstance(a,(float,int)) or not isinstance (b,(int,float)):
            print("Invalid input")
            return
    # return the sum
    return a+b
#print the result of add (5,3)
print(f"Sum: {add(5,3)}")