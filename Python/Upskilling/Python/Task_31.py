"""
31. Create List
• Objective: Initialize a list with basic validation + a function + clean output.
• Task: Create a shopping cart list and display the items.
"""
def display_cart():
    cart = [100,250,75]
    if len(cart) == 0:
        print("cart is  empty")
    else:
        print("cart items: ")
        for item in cart:
            print(item)
display_cart()
