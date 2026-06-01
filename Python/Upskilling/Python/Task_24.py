from math import *
def math_operations(num):
    #validate input
    if not isinstance(num,(int,float)):
        print("Invalid input")
        return
    if num <0:
        print("Number must be non-negative")
        return
    # demonstarte math operations
    square_root = sqrt(num)
    power = pow(num,2)

    # Display results
    print(f"Square Root: {square_root}")
    print(f"Power : {power}")
    print(f"Value of pi: {pi:.2f}")
math_operations(9)
