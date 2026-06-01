"""
For Loop Basics
Objective: Iterate a fixed number of times with a function + validation + formatted output.
Task: Print numbers from 1 to 5 using range().
"""
def print_numbers(count):
    if type(count) != int :
        print("Invalid input")
        return
    if count <=0:
        print("count must be greater than zero")
        return
    for i in range(1,count+1):
        print(f" numbers :{i}")
print_numbers(5)