"""
Nested Dictionary
• Objective: Work with nested dictionaries using a function and basic validation.
• Task: Store department-wise employee data and retrieve a specific employee’s salary.
"""
def get_salary():
    employees = {
        "IT":{
            "Alice":60000,
            "Bob" : 55000
        },
        "HR" : {
            "Charlie":50000,
            "Diana" : 45000
        }
    }
    department = "IT"
    employee = "Alice"
    if department in employees:
        if employee in employees[department]:
            salary = employees[department][employee]
            print("salary: ",salary)
        else:
            print("Employee not found")
    else:
        print("Department not found")
get_salary()