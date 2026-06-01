"""
Modulo Operator
• Objective: Use the modulo operator with function + validation + clean output.
• Task: Check if a number is even or odd using %.
"""
num = 17
def checknum(num):
    if type(num)!=int :
        print("Invalid input")
        return
    if num%2==0 :
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
checknum(num)