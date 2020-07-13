# Check the marks of the user, when mark is 1, the student 
# has to repeat the class

history = float(input("Type your history mark: "))
physics = float(input("Type your physics mark: "))
math = float(input("Type your math mark: "))

list_of_grades = []
list_of_grades.append(history)
list_of_grades.append(physics)
list_of_grades.append(math)
print()
for grade in list_of_grades:
    if grade == 1:
        print("You didn't pass")
        break
else:        
    print("You've passed")



