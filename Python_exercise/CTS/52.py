students = {
    "Srishti": [90, 85, 88],
    "Rahul": [70, 75, 80]
}

def calculate_gpa(grades):
    return sum(grades) / len(grades)

for student, grades in students.items():
    print(student, "GPA:", calculate_gpa(grades))

class_average = sum(
    calculate_gpa(grades) for grades in students.values()
) / len(students)

print("Class Average:", class_average)