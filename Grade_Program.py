# Grade Program

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


try:
    score = float(input("Enter your numeric grade (0-100): "))

    if 0 <= score <= 100:
        grade = get_letter_grade(score)
        print(f"Your letter grade is: {grade}")
    else:
        print("Error: Please enter a score between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
