# Get from the use categories of expenditures and for each
# of them expeditures (use while loop). Using for loop 
# calculate total expenditure and
# percentage of expenditures in monthly budget
# Write down the numbers, and choose the most important category

expenditures = {}
category_name = input("Type the name of the category, when done type ""X"": ")
while category_name != "X":
    expenditures[category_name] = []
    expenditure = input(f"Type how much you spend on {category_name}, or exit with ""X"": ")
    while expenditure != "X":
        expenditure_value = float(expenditure)
        expenditures[category_name].append(expenditure_value)
        expenditure = input(f"Type how much you spend on {category_name}, or exit with ""X"": ")
    category_name = input("Type the name of the category, when done type ""X""")

total_expenditure = 0
for category_expenditures in expenditures.values():
    for expenditure_value in category_expenditures:
        total_expenditure += expenditure_value

expenditure_in_percentage = {}
for category_name, category_expenditures in expenditures.items():
    total_category_expenditure = 0
    for expenditure_value in category_expenditures:
        total_category_expenditure += expenditure_value
    expenditure_in_percentage[category_name] = total_category_expenditure * 100/ total_expenditure

most_important_category = None
most_important_category_percentage = 0

for category, percentage in expenditure_in_percentage.items():
    if percentage > most_important_category_percentage:
        most_important_category_percentage = percentage
        most_important_category = category

if most_important_category is not None:
    print(f"You spend most on {most_important_category} - {most_important_category_percentage:.0f}% of your expenditures")

for category, percentage in expenditure_in_percentage.items():
    print(f"On each {category} you spend {percentage:.0f}% of your monthly money")


