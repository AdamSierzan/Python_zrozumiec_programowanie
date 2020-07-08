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


most_important_category = "food"
if expenditures_percentage["food"] > expenditures_percentage[most_important_category]:
    most_important_category = "food"
if expenditures_percentage["bills"] > expenditures_percentage[most_important_category]:
    most_important_category = "bills"
if expenditures_percentage["fun"] > expenditures_percentage[most_important_category]:
    most_important_category = "fun"
if expenditures_percentage["other"] > expenditures_percentage[most_important_category]:
    most_important_category = "other"

print(f"On {most_important_category} you spend {expenditures_percentage[most_important_category]:.0f}% of your total expenditures")