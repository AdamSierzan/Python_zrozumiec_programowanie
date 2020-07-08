# AND OPERATOR

name = input("Type your name")

name_lenght = len(name)

if name_lenght < 5:
    print(f"{name} is a short name")
if 5 <= name_lenght <= 8:
    print(f"{name} is a regular lenght name")
else:
    print(f"{name} is a long name")

    
    
born_as_usa_citizen_answer = input("Are you a native American? (T/N) ")
age = int(input("How old are you? "))
usa_residence_years = int(input("How long you live in the USA"))

if born_as_usa_citizen_answer == "T":
    born_as_usa_citizen = True
else:
    born_as_usa_citizen = False

if born_as_usa_citizen and age >= 35 and usa_residence_years >= 14:
    print("You can be a candidate")
else:
    print("You can't run for president")

# OR OPERATOR

# if income <15000 or (number_of_employees >= 3 and income <33000):
#     print("You can get a donation")

# else:
#     print("You can't get a donation")


# NOT OPERATOR


income = float(input("What's your monthly income"))
number_of_employees = int(input("How many employees you hire "))
support_answer = input("Have your company recieved a donation before ""Y/N""")

if support_answer == "T":
    support_used = True
else:
    support_used = False

if not support_used and (income < 15500 or number_of_employees >= 3):
    print("You can get a donation")
else:
    print("You can't get a donation")


if not 3 < 2:
    print("3 nie jest mniejsze od 2")


income = 4000
expenditures = 2000
age = 30

if age < 18 or income < expenditures:
    print("You can't get a loan")
else:
    print("You can get a load")

if not (age < 18 or income < expenditures):
    print("You can get a loan")
else:
    print("You can't get a loan")
