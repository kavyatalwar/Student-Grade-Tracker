# Student Grade Tracker Program

def calculate_average(grades):
    return sum(grades) / len(grades)

def determine_letter_grade(average):
    if 90 <= average <= 100:
        return 'A'
    elif 75 <= average < 90:
        return 'B'
    elif 50 <= average < 75:
        return 'C'
    elif average < 40:
        return 'D'
    else:
        return 'Failed'

def determine_gpa(letter_grade):
    gpa_scale = {'A': 9.0, 'B': 7.5, 'C': 5.0, 'D': 4.0, 'Failed': '<4.0'}
    return gpa_scale.get(letter_grade, "No GPA available for invalid grade")

def student_grade_tracker():
    print("Student Grade Tracker")

    subjects = int(input("Enter the number of subjects or assignments: "))
    grades = []

    # Input grades for each subject or assignment
    for i in range(subjects):
        grade = float(input(f"Enter grade for subject {i+1}: "))
        grades.append(grade)

    # Calculate average grade
    average_grade = calculate_average(grades)

    # Determine letter grade and GPA
    letter_grade = determine_letter_grade(average_grade)
    gpa = determine_gpa(letter_grade)

    # Display results
    print("\n=== Grade Report ===")
    print(f"Average Grade: {average_grade:.2f}")
    print(f"Letter Grade: {letter_grade}")
    print(f"GPA: {gpa}")

# Run the grade tracker
student_grade_tracker()
