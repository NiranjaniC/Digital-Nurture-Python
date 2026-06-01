"""
Basic Input
• Objective: Read and validate user input using a function + formatted output.
• Task: Get the user’s name and greet them.
"""
def greet_user():
    name = input("Enter user name: ")
    if name == "":
        print("Invalid input")
        return
    print(f"Hello, {name}")
greet_user()
