# Write the calculator of decreasing installment
# Ask for:
# capital
# intrest_rate
# years
# initial cost, comission
# Calculate how much money the user will give back to the bank
# Compare it with the money he'll get

# Monthly installment formula:
# monthly_paid_capital = capital / (years *12)
# capital_to_be_paid = capital - (number of month from beginning -1) * monthly_paid_capital
# installment = (capital_to_be_paid *intrest_rate / 100% / 12 + monthly_paid_capital)

capital = int(input("What's the value of the loan"))
intrest_rate = float(input("What's the intrest rate of the loan"))
years = int(input("For how many years you want to loan the money"))
initial_cost = int(input("What are initial costs"))

credit_time_in_months = years * 12
monthly_paid_capital = capital/ credit_time_in_months

total_paid = initial_cost

for month_number in range(1, credit_time_in_months +1):
    capital_to_be_paid = capital - (month_number -1) * monthly_paid_capital
    installment = (capital_to_be_paid * intrest_rate /100) / 12 + monthly_paid_capital
    total_paid += installment
    print(f"Installment in{month_number} will be {installment:.2f}")

print(f"By taking {capital} on you'll pay {total_paid} will installments")


