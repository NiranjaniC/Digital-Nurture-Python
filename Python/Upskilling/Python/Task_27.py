"""
Len Function
• Objective: Use len() inside a function with basic validation + structured output.
• Task: Get the length of a given string.
"""
def get_length(text):
    if not isinstance(text,str):
        print("Invalid input")
        return
    # get and print the length
    length = len(text)
    print(f"Length: {length}")
get_length("Hello")