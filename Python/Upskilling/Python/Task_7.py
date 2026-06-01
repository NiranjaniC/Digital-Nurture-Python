"""
Floor Division
• Objective: Perform integer division with function + validation + formatted output.
• Task: Split a total bill equally among people.
"""
def split_bill(total_bill,people):
    if type(total_bill)!=int and type(total_bill)!=float:
        print("Invalid bill amount")
        return
    if type(people)!=int or people <= 0 :
        print("Invalid number of people")
        return
    share = total_bill//people
    print(f"Total Bill : {total_bill}")
    print(f"No of people : {people}")
    print(f"Each Share : {share}")
total_bill = 1250
people = 4
split_bill(total_bill,people)
