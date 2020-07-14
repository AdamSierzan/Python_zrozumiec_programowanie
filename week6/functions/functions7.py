
def find_best_grade(grades_by_subject):
    best_subject = None
    best_grade = 0
    for subject, grades in grades_by_subject.items():
        best_grade_from_subject = max(grades)
        if best_grade_from_subject > best_grade:
            best_grade = best_grade_from_subject
            best_subject = subject
    return best_grade, best_subject


grades_data = {
    "History": [5, 5, 4, 5],
    "Math": [5, 4, 3, 6],
    "Physics": [4, 3, 2, 5]
}
 the_best_grade, subject = find_best_grade(grades_data)
print(f"Best grade is  {the_best_grade} and it's  {subject} grade")

result = find_best_grade(grades_data)
print(result[0])
print(type(result))