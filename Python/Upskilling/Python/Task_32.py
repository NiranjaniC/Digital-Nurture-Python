"""
Append to List
• Objective: Add a single item to a list using a function with validation.
• Task: Add a new expense to an existing expenses list.
"""
def add_expenses():
    expenses = [100,250,75]
    new = 300
    if(new > 0):
        expenses.append(new)
        print("Updated expenses:")
        print(expenses)
    else:
        print("Invalid expense amount")
add_expenses()