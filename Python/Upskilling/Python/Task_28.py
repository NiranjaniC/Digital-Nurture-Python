"""
Write to File
• Objective: Create and write to a text file using a function + clean structure.
• Task: Save a greeting message into a text file.
"""
def write_message():
    file =open("greeting.txt","w")
    file.write("Hello world")
    file.close()
    print("Message written successfully")
write_message()
