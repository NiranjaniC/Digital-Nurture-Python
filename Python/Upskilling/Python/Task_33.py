"""
Update Dictionary
• Objective: Perform bulk dictionary updates using a function with basic validation.
• Task: Merge employee details from two dictionaries.Update Dictionary
"""
def merge_employee_data():
    employee1 = {
        "name" : "Niranjani"
    }
    employee2 = {
        "salary" : 50000
    }
    if isinstance(employee1,dict) and isinstance(employee2,dict):
        employee1.update(employee2)
        print("updated Employee Data:")
        print(employee1)
    else:
        print("Invalid dictionary input")
merge_employee_data()
