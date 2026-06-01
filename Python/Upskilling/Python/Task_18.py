"""
Break Statement
Objective: Use break to exit loop early.
Task: Find and print the first even number in a given range.
"""
def find_first_even(limit):
    if type(limit)!=int:
        print("Invalid input!")
        return
    if limit <= 0 :
        print("Limit must be greater than 0 !")
        return
    for i in range(1,limit+1):
        if i % 2 == 0 :
            print(f"First even number : {i}")
            break
find_first_even(10)
