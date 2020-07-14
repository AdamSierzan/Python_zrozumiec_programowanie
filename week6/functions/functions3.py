
def calculate_investment_value(initial_value, percentage, years):
    result = initial_value * (1 + percentage / 100) ** years
    print(f"After {years} yeats your investment will be equal to {result:.2f}")


print("Investment calculator")

initial_value_input = input("What's the initial value? ")
initial_value = int(initial_value_input)
percentage_input = input("What's the percentage rate (%)? ")
percentage = int(percentage_input)
years_input = input("How many years will be be investing? ")
years = int(years_input)

calculate_investment_value(initial_value, percentage, years)


def calculate_alternative_investment_value(initial_value, percentage, years):
    result = initial_value * (1 + percentage / 100) ** years
    print(f"Consider leaving the investment for {years} years - it will be worth {result:.2f}")


calculate_alternative_investment_value(initial_value, percentage, years * 2)
