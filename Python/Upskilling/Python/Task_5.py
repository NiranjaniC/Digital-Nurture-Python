"""
Multiple Assignment
• Objective: Use multiple assignment with basic validation + function + formatted output.
• Task: Unpack (x, y) coordinates and display them.
"""
def display_coordinates(x,y):
    if type(x)!= int and type(x)!=float:
        print("Invalid x cooridnate")
        return
    if type(y)!=int and type(y)!=float:
        print("Invalid y coordinate")
        return
    print(f"X coordinate : {x}")
    print(f"Y coordinate : {y}")
x,y = 10,20
display_coordinates(x,y)