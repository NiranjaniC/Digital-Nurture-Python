"""
If-Else
Objective: Two-way decision using functions + validation + formatted output.
Task: Check if a number is even or odd.
"""
def check_num():
    num = input("E nter a number : ")
    if(num == ""):
        print("Number sould not be empty")
        return
    if not num.isdigit():
        print("Invalid input")
        return
    num= int(num)
    if(num%2==0):
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
check_num()