student_score = {
    "mohammad": 98,
    "reza": 87,
    "erfan": 75,
    "naserrr": 65
}

student_grade = {}


for student in student_score:
    score = student_score[student]
    if score > 90:
        student_grade[student] = "Outstanding"
    elif score > 80:
        student_grade[student] = "Exceede Expectation"
    elif score > 70:
        student_grade[student] = "Acceptable"
    else:
        student_grade[student] = "Fail"

for st in student_grade:
    print(f"The {st} is {student_grade[st]}")

print(student_grade)
