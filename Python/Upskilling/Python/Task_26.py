"""
Multiple Parameters
• Objective: Handle multiple arguments in a function with validation + formatted output.
• Task: Calculate the area of a rectangle using length and width.
"""
def area(length,width):
    #validate inputs
    if not isinstance(length,(int,float)) or not isinstance(width,(int,float)):
        print("Invalid input")
        return
    if length <=0 or width <=0:
        print("Length and width must be greater than 0")
        return 
    # calculate and return area
    return length*width

# print result
print(f"Area: {area(5,3)}")
