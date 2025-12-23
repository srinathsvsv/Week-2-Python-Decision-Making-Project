# Student Grade Calculator
# Week-2 Task - Python Decision-Making & Loops

def grade_calculate(st_marks):
    if 90 <= st_marks <= 100:
        return "A", "Excellent work! Keep shining "
    elif 80 <= st_marks <= 89:
        return "B", "Very Good! Keep it up "
    elif 70 <= st_marks <= 79:
        return "C", "Good effort! You can do even better "
    elif 60 <= st_marks <= 69:
        return "D", "You passed! Keep practicing "
    else:
        return "F", "Don't give up! Learn from mistakes and try again "


# Input student name
student_name = input("Enter student name: ")

# Input validation

while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("Please enter marks between 0 and 100 only.")
    except ValueError:
        print("Invalid input. Please enter numeric value.")

# Calculate grade
grade, message = grade_calculate(marks)

# Display result
print("\n📊 RESULT FOR", student_name.upper())
print("Marks:", marks, "/100")
print("Grade:", grade)
print("Message:", message)
