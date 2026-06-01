"""
Consistent Indentation
• Objective: Demonstrate clean, consistent indentation using a nested if inside a
function.
• Task: Print "Nested" when both conditions are True.
"""
def check_nested():
    condition1 = True
    condition2 = True
    if condition1:
        if condition2:
            print("Nested")
    print("Confirmation : Function executed")
check_nested()