"""
Min/Max Functions
• Objective: Use built-in min() and max() with validation + function + structured output.
• Task: Find the highest and lowest salary in a list.
"""
def Salary(salaries):
    if type(salaries)!=list:
        print("Invalid salary input")
        return
    if len(salaries)==0:
        print("Salary is empty")
        return
    highest = max(salaries)
    print(f"Highest Salary : {highest}")
    lowest = min(salaries)
    print(f"Lowest Salary : {lowest}")
salaries = [50000,75000,62000,95000]
print(f"Salary List : {salaries}")
Salary(salaries)


