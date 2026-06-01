"""
Continue Statement
• Objective: Use continue to skip even numbers, with a function + validation + formatted
output.
• Task: Sum only the odd numbers in a given range.
"""
def sum_of_odd(limit):
    if type(limit)!=int:
        print("Invalid input")
        return 
    if limit <0:
        print("limit must e greater than zero")
        return
    sum=0
    for i in range(1,limit+1):
        if i % 2 == 0 :
            continue
        sum +=i
    print(f"Sum of odd numbers : {sum}")
sum_of_odd(10)
       
