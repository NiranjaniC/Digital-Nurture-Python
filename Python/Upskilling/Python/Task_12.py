"""
Simple If
• Objective: Basic conditional with function, validation, and user interaction.
• Task: Check if a student passes based on marks.
"""
def check_result():
    marks = input("Enter marks")
    if marks == "":
        print("Marks cannot be empty")
        return
    if not marks.isdigit():
        print("Invalid input")
        return
    marks = int(marks)
    if(marks< 0) or (marks >100):
        print("Mark must be between 0 to 100")
        return
    if(marks >= 50):
        print(f"Marks : {marks} - pass")
    else:
        print(f"Marks : {marks} - fail")
check_result()

