# We use break to get out of the loop in python 
# Python will get automatically to the next line, out of the loop
# We use break to search for an element, without knowing if it's in the loop

expenditures = [120, 300, 255.52, 1300]

for expenditures in expenditures:
    if expenditures >1000:
        print("Expensive expenditure found")
        break

# With for loops we have else as well

for expenditures_2 in expenditures:
    if expenditures > 1000:
        print("Expensive expenditure found")
        break
else:
    print("Nothing found")


# Break to break w  hile loop
grades = []
while True:
     grade_input = input("Type another mark or type 'X' for exit: ")
     if grade_input == "X":
         break
     grade = int(grade_input)
     grades.append(grade)

 grades_sum = sum(grades)
 average = grades_sum / len(grades)
 print(f"You're average is: {average:.2f}")

# While loops also have else
grades = []
 while len(grades) < 5:
     grade_input = input("Give me another mark or type 'X': ")
     if grade_input == "X":
         break
     grade = int(grade_input)
     grades.append(grade)
 else:
     print("That's enough :)")

 grades_sum = sum(grades)
 average = grades_sum / len(grades)
 print(f"Your avg is : {average:.2f}")