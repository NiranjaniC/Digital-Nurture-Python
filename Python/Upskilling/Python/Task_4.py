"""
Float Precision
• Objective: Handle floating-point arithmetic with functions + validation + formatted
output.
• Task: Calculate net salary after tax and print with 2 decimals.
"""
salary = 75000.5
tax_rate = 0.18
def calculate_net_salary(salary,tax_rate):
    if salary<=0 :
        print("Invalid salary")
        return
    if tax_rate <=0:
        print("Invalid tax rate")
        return
    tax = salary*tax_rate
    net_salary = salary - tax
    print(f"Gross salary : {salary:.2f}")
    print(f"Tax Deducted : {tax:.2f}")
    print(f"Net salary  : {net_salary:.2f}")
calculate_net_salary(salary,tax_rate)
    