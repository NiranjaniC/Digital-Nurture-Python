"""
Nested If
Objective: Use nested conditions with a function + validation + formatted output.
Task: Validate username and password using nested if statements.
"""
def login():
    username = input("Enter a username:")
    password = input("Enter password: ")
    if username == "":
        print("Username cannot be empty")
        return
    if password == "":
        print("password cannot be empty")
    if username =="admin":
        if password == "123pass":
            print("Login successfully")
        else:
            print("Wrong password")
    else:
        print("username not found")
login()