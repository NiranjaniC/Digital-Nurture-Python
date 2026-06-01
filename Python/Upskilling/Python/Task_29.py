"""
29. Read from File
• Objective: Read text from a file using a function with basic error handling.
• Task: Open a text file and display its contents.
"""
def read_message():
    try:
        file = open("greeting.txt","r")
        content = file.read()
        print(content)
        file.close()
    except FileNotFoundError:
        print("File not Found")
read_message()
