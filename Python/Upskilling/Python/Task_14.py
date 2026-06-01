"""
If-Elif-Else
Objective: Multi-way decision using functions + validation + structured output.
Task: Assign a grade based on the score.
"""
def assign_grade():
    score = input("Enter score: ")
    if score == "":
        print("Score cannot be empty")
        return
    if not score.isdigit():
        print("Invalid input")
        return
    score = int(score)
    if score < 0  or score >100:
        print("score must be between 0 to 100")
        return
    if(score >= 90):
        grade = "A"
    elif score >=80:
        grade = 'B'
    elif score >=70:
        grade = "C"
    elif score >= 50 :
        grade ="D"
    else:
        grade = "F"
    print(f"Score : {score}")
    print(f"Grade : {grade}")
assign_grade()