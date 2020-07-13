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
