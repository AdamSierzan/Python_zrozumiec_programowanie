food = float(input("How much did you spend on food this month: "))
bills = float(input("How much did you spend on bills this month: "))
fun = float(input("How much did you spend on fun this month: "))
other = float(input("How much did you spend on other things this month: "))

to_sum_up  = food + bills + fun + other
print(to_sum_up)

expenditures_percentage = {
    "food": food*100 / to_sum_up,
    "bills": bills*100 / to_sum_up,
    "fun": fun*100 / to_sum_up,
    "other": other*100 / to_sum_up,
}


selected_category = input("Choose one of the categories from: food, bills, fun, other")

print(f"On {selected_category} you spend {expenditures_percentage[selected_category]:.0f}% of your total expenditures")