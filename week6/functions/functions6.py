# We can go ever further and put the rest of the code into the function

def calculate_investment_value(initial_value, percentage, years):

    return initial_value * (1 + percentage / 100) ** years

# We can also make a function that will let us insert values to the programm

def ask_for_int_value(message):
    input_value = input(message)
    return int(input_value)

def run_investment_calculator():
    print("Investment calculator")

    initial_value = ask_for_int_value("What's the initial value? ")
    percentage = ask_for_int_value("What's the percentage rate (%)? ")
    years = ask_for_int_value("How many years will be be investing? ")


    final_value = calculate_investment_value(initial_value, percentage, years)
    print(f"After {years} years your investment will be equal to {final_value:.2f}")

    longer_term = years * 2
    alternative_value = calculate_investment_value(initial_value, percentage, longer_term)
    print(f"Consider leaving the investment for {years} years - it will be worth {alternative_value:.2f}")
 
option = None
while option != "X":
    run_investment_calculator()
    option = input("To quit the calculator type ""X"", type other character to continue")