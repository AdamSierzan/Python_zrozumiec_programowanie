
# Zmodyfikuj zadanie dotyczÄ…ce budÅ¼etu domowego â€œzamykajÄ…câ€ spÃ³jne elementy programu w funkcje.

print("Monthly expenditure calculator")

def load_expenditures(category_name):
    expenditures_values = []
    while True:

        expenditure = input(f"Type the value of next expenditure in category {category_name} or quit with 'X': ")
        if expenditure == "X":
            return expenditures_values

        expenditure_value = float(expenditure)
        expenditures_values.append(expenditure_value)


def load_expenditures_by_categories():
    expenditures = {}
    while True:
        category_name = input("Type the category of expenditure or quit with 'X': ")
        if category_name == "X":
            return expenditures

        expenditures[category_name] = load_expenditures(category_name)


def calculate_total_expenditures(expenditures):
    result = 0
    for category_expenditures in expenditures.values():
        result += sum(category_expenditures)
    return result


def calculate_expenditures_percentages(expenditures, total_expenditures):
    percentages_by_category_name = {}
    for category_name, category_expenditures in expenditures.items():
        total_category_expenditures = sum(category_expenditures)
        percentages_by_category_name[category_name] = total_category_expenditures * 100 / total_expenditures
    return percentages_by_category_name


def find_most_important_category(percentages_by_category_name):
    highest_percentage_category = None
    highest_percentage = 0
    for category, percentage in percentages_by_category_name.items():
        if percentage > highest_percentage:
            highest_percentage = percentage
            highest_percentage_category = category
    return highest_percentage_category, highest_percentage


def print_most_important_category_info(category_name, percentage):
    print(f"You spend most money on {category_name} - {percentage:.0f}% of all expenditures")


def print_category_info(category, percentage):
    print(f"On {category} you spend {percentage:.0f}% monthly expenditures")


expenditures_by_categories = load_expenditures_by_categories()
total_expenditures = calculate_total_expenditures(expenditures_by_categories)
expenditures_percentage = calculate_expenditures_percentages(expenditures_by_categories, total_expenditures)
most_important_category, most_important_category_percentage = find_most_important_category(expenditures_percentage)

if most_important_category is not None:
    print_most_important_category_info(most_important_category, most_important_category_percentage)

for category, percentage in expenditures_percentage.items():
    print_category_info(category, percentage)