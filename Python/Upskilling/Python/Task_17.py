"""
While Loop
Objective: Use a condition-based loop with validation + function + formatted output.
Task: Countdown from 5 to 1 using a while loop.
"""

def countdown(count):
    if type(count)!=int:
        print("Invalid input")
        return
    if count <=0:
        print("count must be greater than zero")
        return
    while count > 0:
        print(f"count : {count}")
        count-=1
    print("Done!")
countdown(3)