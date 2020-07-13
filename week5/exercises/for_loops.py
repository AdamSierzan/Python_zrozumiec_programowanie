# ASk the user for grades, use while loop to ask for next grade, and
# to end it when he types X. Check the average of grades
counter  = 1
grades = []
while counter:
    grade = (input("Type your math grades, if you want to quit type ""X"": "))
    if grade == "X":
        counter = 0
    else:
        grades.append(grade)
print(grades)

sum_of_grades = 0
for item in grades:
    sum_of_grades += int(item)
print(sum_of_grades/len(grades))
