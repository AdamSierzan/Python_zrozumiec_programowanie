# Hi! This program can calculate your invested money and tell you if you can get a load.

loan_or_invesment = input("To calculate your investment type ""I"" to check if you can get a credit type ""C"" ")

if loan_or_invesment == "I":
    balance  = int(input((1000)))
    rate = 0.04
    after_5_years = balance * (1 + rate) ** 5 
    print(f"Your balance after 5 years will be: {after_5_years:.2f}")
    print(f"Your balance after 5 years will be raise by 10% {after_5_years==balance+ balanc*0.1}")

elif loan_or_invesment == "C":

    loan_amount = float(input("How much you want to loan"))
    rate = float(input(("What's the credit rate")))
    own_contribution = float(input("what's your own contribution"))
    years_of_crediting = int(input("How many years you want to spend on crediting"))
    monthly_income = float(input("What's your monthly income"))
    monthly_expenditure = float(input("What's your monthly expenditures"))

    installment_value = (loan_amount*rate / 100) * 12 + loan_amount / (years_of_crediting *12)

    money_to_use = monthly_income - monthly_expenditure

    value_of_real_estate = own_contribution + loan_amount

    own_contribution_part = own_contribution / value_of_real_estate

    money_over_installment = money_to_use - installment_value

    if own_contribution_part >= 0.2 and money_over_installment >= 1000:
        print("You can get a credit")

    if own_contribution_part*0.1 and money_over_installment >= 2000:
        print("You can get a credit")
    if value_of_real_estate*0.1 > own_contribution_part:
        print("You cant get a credit")

else:
    print("Seems like I can't help")

